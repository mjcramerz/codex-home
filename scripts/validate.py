#!/usr/bin/env python3
"""Validate every active config against the EXACT supplied custom schema.

This additionally validates typed permission-profile internals that the schema's
open map cannot validate, instruction references, all features and preserved assets.
No download, inferred latest version, model substitution, or prompt removal occurs.
"""
from __future__ import annotations
import argparse
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import tomllib
ROOT=Path(__file__).resolve().parents[1]

def load(path: Path):return tomllib.loads(path.read_text())
def sha(path: Path):return hashlib.sha256(path.read_bytes()).hexdigest()
def assert_ok(condition: bool,message: str) -> None:
    if not condition:raise ValueError(message)
def objects(obj,path=()):
    if isinstance(obj,dict):
        yield path,obj
        for k,v in obj.items():yield from objects(v,(*path,k))
    elif isinstance(obj,list):
        for i,v in enumerate(obj):yield from objects(v,(*path,i))

def active_files(root: Path=ROOT):
    return [*sorted((root/'home').glob('*.toml')),*sorted((root/'agents').glob('*.toml')),root/'etc/config.toml']

def validate_data(data: dict,schema: dict,policy: dict,label: str) -> None:
    import jsonschema
    validator=jsonschema.Draft7Validator(schema)
    errors=list(validator.iter_errors(data))
    if errors:
        raise ValueError(label+': '+ '; '.join('/'.join(map(str,e.path))+': '+e.message for e in errors))
    forbidden=set(policy['removed'])|set(policy['deprecated'])|set(policy['aliases'])
    for where,o in objects(data):
        if where and where[-1]=='features':
            bad=set(o)&forbidden
            assert_ok(not bad,f'{label}: active obsolete feature flags at {where}: {sorted(bad)}')
        if where and where[-1]=='multi_agent_v2':
            assert_ok('usage_hint_enabled' not in o,f'{label}: ignored usage_hint_enabled field')
    assert_ok(not ('default_permissions' in data and 'sandbox_mode' in data),f'{label}: competing permission selectors')
    for name,profile in data.get('permissions',{}).items():
        # PermissionsToml is intentionally an open object, so check its named entries explicitly.
        sub={'$ref':'#/definitions/PermissionProfileToml','definitions':schema['definitions']}
        jsonschema.Draft7Validator(sub).validate(profile)
        for target,mode in profile.get('filesystem',{}).items():
            if target=='glob_scan_max_depth':continue
            sub={'$ref':'#/definitions/FilesystemPermissionToml','definitions':schema['definitions']}
            jsonschema.Draft7Validator(sub).validate(mode)
        network=profile.get('network',{})
        for field,definition in [('domains','NetworkDomainPermissionToml'),('unix_sockets','NetworkUnixSocketPermissionToml')]:
            for value in network.get(field,{}).values():
                jsonschema.Draft7Validator({'$ref':'#/definitions/'+definition,'definitions':schema['definitions']}).validate(value)

def validate(root: Path=ROOT,write: bool=True) -> dict:
    import jsonschema
    schema_path=root/'generate/schemas/config.schema.json'
    schema=json.loads(schema_path.read_text());jsonschema.Draft7Validator.check_schema(schema)
    policy=json.loads((root/'generate/feature-policy.json').read_text())
    assert_ok(sha(schema_path)==policy['schema_sha256'],'schema checksum is not the supplied custom schema')
    for rel in ('home/config.schema.json','etc/config.schema.json','generate/schemas/supplied-config.schema.json'):
        assert_ok(sha(root/rel)==sha(schema_path),f'schema mirror mismatch: {rel}')
    configs=active_files(root);refs=[];results=[]
    for path in configs:
        data=load(path);label=path.relative_to(root).as_posix();validate_data(data,schema,policy,label)
        results.append({'file':label,'schema':'exact supplied Draft-07','ok':True})
        for where,o in objects(data):
            for key,value in o.items():
                if isinstance(value,str) and (key.endswith('_file') or key=='model_catalog_json'):
                    if value.startswith('/data/codex/usr/'):
                        local=root/value.removeprefix('/data/codex/usr/')
                        assert_ok(local.is_file(),f'{label}: missing instruction/catalog/agent file {value}')
                        refs.append({'config':label,'key':'.'.join(map(str,(*where,key))),'installed_path':value,'source':local.relative_to(root).as_posix()})
                    elif key.endswith('_file'):
                        assert_ok(Path(value).is_absolute(),f'{label}: expected absolute path: {value}')
    home=load(root/'home/config.toml');etc=load(root/'etc/config.toml')
    assert_ok(home==etc,'home/config.toml and etc/config.toml differ')
    expected=set(schema['properties']['features']['properties'])-set(policy['removed'])-set(policy['deprecated'])-set(policy['aliases'])
    assert_ok(set(home['features'])==expected,'main config must include every nondeprecated supplied-schema feature')
    original=load(root/'migration/original-home-config.toml')
    for name in expected:
        old=original['features'][name]
        if isinstance(old,dict):old={k:v for k,v in old.items() if k!='usage_hint_enabled'}
        assert_ok(home['features'][name]==old,f'original feature value changed: {name}')
    for key in ('model','review_model','model_provider','model_providers','developer_instructions','instruction_overrides',
                'model_catalog_json','model_instructions_file','experimental_compact_prompt_file','agents',
                'apps','skills','plugins','realtime','audio','tui','memories','auto_review'):
        assert_ok(home[key]==original[key],f'original custom configuration unexpectedly altered: {key}')
    registry=json.loads((root/'mcp/servers.json').read_text());mapping=json.loads((root/'generate/mcp-config-map.json').read_text())
    assert_ok(set(mapping.values())==set(registry),'MCP image modes missing from config mapping')
    assert_ok(set(home['mcp_servers'])==set(original['mcp_servers']),'an original MCP registration was lost')
    for key,name in mapping.items():
        server=home['mcp_servers'][key]
        assert_ok(server['enabled'] and server['command']=='/usr/local/bin/codex-mcp' and server['args']==['connect',name],f'bad local MCP registration: {key}')
        assert_ok(not server.get('env') and not server.get('env_vars'),f'secrets should be loaded by systemd for {key}')
    assert_ok(home['mcp_servers']['node_repl']['env']==original['mcp_servers']['node_repl']['env'],'desktop Node environment was lost')
    req=load(root/'etc/requirements.toml')
    # Narrow project-policy check, not a claim to have an official requirements schema.
    assert_ok(set(req)=={'allow_managed_hooks_only','features'},'unexpected local requirement constraint')
    assert_ok(req['allow_managed_hooks_only'] is False,'custom hooks disallowed by local requirements')
    gates={'browser_use','browser_use_external','browser_use_full_cdp_access','computer_use','in_app_browser','in_app_updates'}
    assert_ok(set(req['features'])==gates and all(v is True for v in req['features'].values()),'desktop requirements gates')
    hooks=json.loads((root/'home/hooks.json').read_text())
    jsonschema.Draft7Validator(schema).validate({'hooks':hooks['hooks']})
    handler_count=0
    for event,groups in hooks['hooks'].items():
        for group in groups:
            for handler in group['hooks']:
                handler_count+=1
                paths=re.findall(r'\$CODEX_HOME/([^"\s]+)',handler['command'])
                assert_ok(bool(paths),f'no source path in {event} hook')
                for path in paths:assert_ok((root/'home'/path).is_file(),f'missing hook script: {path}')
    for path in (root/'instructions').rglob('*'):
        if path.is_file():
            mirror=root/'home/instructions'/path.relative_to(root/'instructions')
            assert_ok(mirror.is_file() and path.read_bytes()==mirror.read_bytes(),f'instruction mirror mismatch: {path}')
    preserved=json.loads((root/'migration/original-files.json').read_text());missing=[];changed=[];same=[]
    for rel,digest in preserved.items():
        p=root/rel
        if not p.is_file():missing.append(rel)
        elif sha(p)!=digest:changed.append(rel)
        else:same.append(rel)
    assert_ok(not missing,'original source files missing: '+', '.join(missing))
    original_instructions=[x for x in preserved if x.startswith('instructions/')]
    assert_ok(all(x in same for x in original_instructions),'an original instruction source was overwritten')
    for folder in ('mcp/lib','mcp/container','mcp/scripts','scripts'):
        for p in (root/folder).glob('*.py'):ast.parse(p.read_text(),filename=str(p))
    report={'target':'custom Codex based on 0.147.0','schema_used':'generate/schemas/config.schema.json',
        'schema_sha256':sha(schema_path),'schema_provenance':'byte-for-byte user attachment; no upstream substitution',
        'active_configuration_files':len(configs),'main_config_lines':len((root/'home/config.toml').read_text().splitlines()),
        'schema_feature_keys':len(schema['properties']['features']['properties']),'active_feature_keys':len(expected),
        'feature_dispositions':{'removed':len(policy['removed']),'deprecated':len(policy['deprecated']),'legacy_aliases':len(policy['aliases'])},
        'instruction_catalog_agent_references':len(refs),'original_instruction_files_unchanged':len(original_instructions),
        'mcp_registrations':len(home['mcp_servers']),'podman_mcp_servers':len(mapping),'plugins_configured':len(home['plugins']),
        'hook_events':len(hooks['hooks']),'hook_handlers':handler_count,
        'original_files':len(preserved),'original_files_present':len(preserved)-len(missing),'original_files_unchanged':len(same),
        'original_files_modified':changed,'missing_original_files':missing,'results':results,
        'requirements_check':'TOML + explicit nonrestrictive project-policy checks; separate from config.schema.json',
        'live_engine_tested':False,'live_podman_tested':False,
        'remaining':'Run target dependency, executable/resource, effective custom-client configuration and live MCP checks.'}
    if write:
        (root/'validation').mkdir(exist_ok=True)
        (root/'validation/static-report.json').write_text(json.dumps(report,indent=2)+'\n')
        (root/'validation/instruction-references.json').write_text(json.dumps(refs,indent=2)+'\n')
        coverage={'top_level':{k:('active' if k in home else 'optional, alternate, product-owned or compatibility-only; see CONFIG-COVERAGE.md') for k in schema['properties']},
                  'features':{k:('active' if k in expected else 'removed' if k in policy['removed'] else 'deprecated' if k in policy['deprecated'] else 'legacy alias') for k in schema['properties']['features']['properties']}}
        (root/'validation/schema-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
    return report

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--no-write',action='store_true');args=p.parse_args()
    try:
        r=validate(write=not args.no_write)
        print(f"PASS: {r['active_configuration_files']} config layers, {r['active_feature_keys']} retained feature keys, {r['mcp_registrations']} MCP entries ({r['podman_mcp_servers']} Podman).")
        print(f"PASS: {r['original_instruction_files_unchanged']} unchanged original instruction files; {r['hook_events']} hook events / {r['hook_handlers']} handlers; all {r['original_files']} original files present.")
        print('Schema SHA256: '+r['schema_sha256'])
        return 0
    except Exception as exc:
        print('VALIDATION FAILED: '+str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
