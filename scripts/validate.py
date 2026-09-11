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

CATALOG_NAMES=('default_catalog.json','cyber_catalog.json','review_catalog.json')
CATALOG_METADATA_SOURCE_VERSION='0.154.0'
CATALOG_MEMBERS={
    'default_catalog.json': (
        'gpt-6-astra','gpt-5.6-sol','gpt-5.6-terra','gpt-5.6-luna',
        'gpt-5.6-cyber','gpt-daybreak-blue-latest','gpt-daybreak-red-latest',
        'codex-auto-review',
    ),
    'cyber_catalog.json': (
        'gpt-5.6-cyber','gpt-daybreak-blue-latest','gpt-daybreak-red-latest',
        'gpt-5.6-sol','codex-auto-review',
    ),
    'review_catalog.json': (
        'gpt-6-astra','gpt-5.6-sol','gpt-5.6-terra','codex-auto-review',
    ),
}
CANONICAL_CATALOG_PATHS=frozenset(
    f'{prefix}/{name}'
    for prefix in ('instructions/models','home/.models')
    for name in CATALOG_NAMES
)
LEGACY_CATALOG_PATHS=frozenset({
    'home/.models/instructions/models/cyber_catalog.json',
    'home/.models/instructions/models/default_catalog.json',
    'home/.models/instructions/models/review_catalog.json',
    'home/instructions/agents/models/default_catalog.json',
    'home/instructions/default/models/default_catalog.json',
    'home/instructions/models/cyber_catalog.json',
    'home/instructions/models/default_catalog.json',
    'home/instructions/models/review_catalog.json',
    'home/instructions/profiles/cyber/models/cyber_catalog.json',
    'home/instructions/profiles/cyber/models/default_catalog.json',
    'home/instructions/profiles/debug/models/default_catalog.json',
    'home/instructions/profiles/fast/models/default_catalog.json',
    'home/instructions/profiles/review/models/default_catalog.json',
    'home/instructions/profiles/review/models/review_catalog.json',
    'home/instructions/profiles/test/models/default_catalog.json',
    'instructions/agents/models/default_catalog.json',
    'instructions/default/models/default_catalog.json',
    'instructions/profiles/cyber/models/cyber_catalog.json',
    'instructions/profiles/cyber/models/default_catalog.json',
    'instructions/profiles/debug/models/default_catalog.json',
    'instructions/profiles/fast/models/default_catalog.json',
    'instructions/profiles/review/models/default_catalog.json',
    'instructions/profiles/review/models/review_catalog.json',
    'instructions/profiles/test/models/default_catalog.json',
})
RETIRED_RUNTIME_ASSETS=LEGACY_CATALOG_PATHS|{'home/spark.config.toml'}
RETIRED_MODELS=frozenset({
    'gpt-5.3-codex-spark','gpt-5.4-mini','gpt-5.4','gpt-5.5','gpt-5.5-cyber',
})
MODEL_REQUIRED_FIELDS=frozenset({
    'prefer_websockets','support_verbosity','default_verbosity',
    'apply_patch_tool_type','web_search_tool_type','input_modalities',
    'supports_image_detail_original','truncation_policy','supports_parallel_tool_calls',
    'context_window','max_context_window','auto_compact_token_limit',
    'effective_context_window_percent','comp_hash','reasoning_summary_format',
    'default_reasoning_summary','slug','display_name','description',
    'default_reasoning_level','supported_reasoning_levels','shell_type',
    'visibility','minimal_client_version','supported_in_api','availability_nux',
    'upgrade','priority','base_instructions','model_messages',
    'experimental_supported_tools','available_in_plans','supports_reasoning_summaries',
    'additional_speed_tiers','service_tiers','include_skills_usage_instructions',
    'include_plugin_usage_instructions','include_apps_usage_instructions',
    'supports_search_tool','supports_experimental_context','use_responses_lite',
    'node_repl_auto_review_required','node_repl_disabled','tool_mode',
    'multi_agent_version',
})

from config_toml import clean_load, clean_loads

def load(path: Path):return clean_load(path)
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

def validate_model_catalogs(root: Path=ROOT) -> dict[str,tuple[str,...]]:
    found={
        path.relative_to(root).as_posix()
        for path in root.rglob('*_catalog.json')
        if path.name in CATALOG_NAMES and (path.is_file() or path.is_symlink())
    }
    assert_ok(found==CANONICAL_CATALOG_PATHS,
              'model catalogs must exist only at canonical source/mirror paths; '
              f'missing={sorted(CANONICAL_CATALOG_PATHS-found)}, extra={sorted(found-CANONICAL_CATALOG_PATHS)}')
    catalogs={};records={}
    for name in CATALOG_NAMES:
        source=root/'instructions/models'/name
        mirror=root/'home/.models'/name
        for role,path in (('source',source),('mirror',mirror)):
            assert_ok(not path.is_symlink() and path.is_file(),f'model catalog {role} is not a regular file: {path}')
        assert_ok(source.read_bytes()==mirror.read_bytes(),f'model catalog mirror mismatch: {name}')
        data=json.loads(source.read_text())
        assert_ok(set(data)=={'models'} and isinstance(data['models'],list),f'invalid model catalog root: {source}')
        models=data['models'];slugs=[]
        for index,model in enumerate(models):
            assert_ok(isinstance(model,dict),f'{source}: model {index} is not an object')
            missing=MODEL_REQUIRED_FIELDS-set(model)
            assert_ok(not missing,f'{source}: model {index} missing fields: {sorted(missing)}')
            slug=model['slug'];assert_ok(isinstance(slug,str) and slug,f'{source}: invalid model slug at {index}')
            slugs.append(slug)
            levels=model['supported_reasoning_levels']
            assert_ok(isinstance(levels,list) and levels and all(isinstance(item,dict) for item in levels),
                      f'{source}: invalid reasoning levels for {slug}')
            efforts=[item.get('effort') for item in levels]
            assert_ok(all(isinstance(effort,str) and effort for effort in efforts) and len(efforts)==len(set(efforts)),
                      f'{source}: invalid or duplicate reasoning efforts for {slug}')
            assert_ok(model['default_reasoning_level'] in efforts,f'{source}: {slug} default reasoning is unsupported')
            assert_ok(0<model['auto_compact_token_limit']<model['context_window']<=model['max_context_window'],
                      f'{source}: invalid context/compaction limits for {slug}')
            assert_ok(isinstance(model['effective_context_window_percent'],int)
                      and 0<model['effective_context_window_percent']<=100,
                      f'{source}: invalid effective context percentage for {slug}')
            tools=model['experimental_supported_tools']
            assert_ok(isinstance(tools,list) and all(isinstance(tool,str) and tool for tool in tools)
                      and len(tools)==len(set(tools)),f'{source}: invalid experimental tools for {slug}')
            assert_ok(model['shell_type']=='unified_exec' and model['tool_mode']=='code_mode_only',
                      f'{source}: current Code Mode metadata missing for {slug}')
            assert_ok(model['supports_search_tool'] is True and model['web_search_tool_type']=='text_and_image',
                      f'{source}: current search metadata missing for {slug}')
            assert_ok(model['use_responses_lite'] is True and model['node_repl_disabled'] is False,
                      f'{source}: current Responses/Node REPL metadata missing for {slug}')
            assert_ok(isinstance(model['base_instructions'],str) and model['base_instructions'],f'{source}: empty base instructions for {slug}')
            messages=model['model_messages']
            assert_ok(isinstance(messages,dict) and isinstance(messages.get('instructions_template'),str),
                      f'{source}: missing instruction template for {slug}')
            assert_ok(slug not in records or records[slug]==model,
                      f'{source}: model record differs from another catalog: {slug}')
            records.setdefault(slug,model)
        assert_ok(len(slugs)==len(set(slugs)),f'{source}: duplicate model slugs')
        assert_ok(tuple(slugs)==CATALOG_MEMBERS[name],f'{source}: unexpected model membership/order: {slugs}')
        assert_ok(not RETIRED_MODELS.intersection(slugs),f'{source}: retired models remain: {sorted(RETIRED_MODELS.intersection(slugs))}')
        catalogs[name]=tuple(slugs)
    astra=records['gpt-6-astra']
    astra_efforts=tuple(item['effort'] for item in astra['supported_reasoning_levels'])
    assert_ok(astra_efforts==('low','medium','high','xhigh','max','ultra'),
              f'GPT-6 Astra reasoning capabilities are incomplete: {astra_efforts}')
    assert_ok(astra['experimental_supported_tools']==['send_user_message_async','clock'],
              'GPT-6 Astra async messaging and clock tools must be enabled')
    assert_ok(astra['prefer_websockets'] is True and astra['supports_experimental_context'] is True,
              'GPT-6 Astra WebSocket steering and experimental context must be enabled')
    assert_ok(astra['node_repl_auto_review_required'] is True and astra['multi_agent_version']=='v2'
              and astra.get('multi_agent_reasoning_effort')=='xhigh',
              'GPT-6 Astra Node REPL review and multi-agent v2 metadata must be enabled')
    assert_ok('fast' in astra['additional_speed_tiers']
              and any(tier.get('id')=='priority' for tier in astra['service_tiers'] if isinstance(tier,dict)),
              'GPT-6 Astra fast service tier metadata must be enabled')
    assert_ok(isinstance(astra['model_messages'].get('persistent_instructions'),str)
              and astra['model_messages']['persistent_instructions'],
              'GPT-6 Astra current persistent system instructions are missing')
    return catalogs

def validate_data(data: dict,schema: dict,policy: dict,label: str) -> None:
    import jsonschema
    validator=jsonschema.Draft7Validator(schema)
    errors=list(validator.iter_errors(data))
    if errors:
        raise ValueError(label+': '+ '; '.join('/'.join(map(str,e.path))+': '+e.message for e in errors))
    forbidden=set(policy['removed'])|set(policy['deprecated'])|set(policy['aliases'])|set(policy.get('requirements_only',[]))
    for where,o in objects(data):
        if where and where[-1]=='features':
            bad=set(o)&forbidden
            assert_ok(not bad,f'{label}: active obsolete feature flags at {where}: {sorted(bad)}')
        if where and where[-1]=='multi_agent_v2':
            assert_ok('usage_hint_enabled' not in o,f'{label}: ignored usage_hint_enabled field')
    assert_ok(not {'experimental_use_unified_exec_tool','ghost_snapshot'} & set(data),f'{label}: obsolete root setting')
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
    catalogs=validate_model_catalogs(root)
    for rel in ('generate/schemas/supplied-config.schema.json',):
        assert_ok(sha(root/rel)==sha(schema_path),f'schema mirror mismatch: {rel}')
    configs=active_files(root);refs=[];results=[]
    for path in configs:
        data=load(path);label=path.relative_to(root).as_posix();validate_data(data,schema,policy,label)
        results.append({'file':label,'schema':'exact supplied Draft-07','ok':True})
        catalog_name=Path(data.get('model_catalog_json','default_catalog.json')).name
        assert_ok(catalog_name in catalogs,f'{label}: unknown model catalog {catalog_name}')
        selected_models=set(catalogs[catalog_name])
        for key in ('model','review_model'):
            if key in data:
                assert_ok(data[key] in selected_models,f'{label}: {key} selects {data[key]!r}, absent from {catalog_name}')
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
    expected=set(schema['properties']['features']['properties'])-set(policy['removed'])-set(policy['deprecated'])-set(policy['aliases'])-set(policy.get('requirements_only',[]))
    assert_ok(set(home['features'])==expected,'main config must include every nondeprecated supplied-schema feature')
    original=load(root/'migration/original-home-config.toml')
    assert_ok(all(home['approval_policy']['granular'].values()),'granular prompt categories must not silently reject')
    assert_ok(not home['features']['unbounded_connection_retries'],'connection retries must be bounded')
    for rel in ('home/config.schema.json','etc/config.schema.json'):
        assert_ok(not (root/rel).exists(),f'build-time config schema must not be installed: {rel}')
    toml_files=sorted(p for p in root.rglob('*.toml') if '__pycache__' not in p.parts)
    for path in toml_files:
        clean_load(path)
    registry=json.loads((root/'mcp/servers.json').read_text());mapping=json.loads((root/'generate/mcp-config-map.json').read_text())
    assert_ok(set(mapping.values())==set(registry),'MCP image modes missing from config mapping')
    assert_ok(set(home['mcp_servers'])==set(original['mcp_servers']),'an original MCP registration was lost')
    for key,name in mapping.items():
        server=home['mcp_servers'][key]
        assert_ok(server['enabled'] and server['command']=='/usr/local/bin/codex-mcp' and server['args']==['connect',name],f'bad local MCP registration: {key}')
        assert_ok(not server.get('env') and not server.get('env_vars'),f'secrets should be loaded by systemd for {key}')
    node=home['mcp_servers']['node_repl']
    assert_ok(node['command']=='/data/codex/usr/home/bin/codex-node-repl','missing validated Node REPL launcher')
    assert_ok(node['env']['NODE_REPL_LAUNCHER'].startswith('/usr/lib/chatgpt/'),'missing explicit bundled REPL path')
    assert_ok(Path(node['env']['NODE_REPL_NODE_PATH']).is_absolute(),'missing explicit Node executable')
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
        if path.is_file() and path.name not in CATALOG_NAMES:
            mirror=root/'home/instructions'/path.relative_to(root/'instructions')
            assert_ok(mirror.is_file() and path.read_bytes()==mirror.read_bytes(),f'instruction mirror mismatch: {path}')
    preserved=json.loads((root/'migration/original-files.json').read_text());missing=[];retired=[];changed=[];same=[]
    for rel,digest in preserved.items():
        p=root/rel
        if not p.is_file():
            if rel in RETIRED_RUNTIME_ASSETS:retired.append(rel)
            else:missing.append(rel)
        elif sha(p)!=digest:changed.append(rel)
        else:same.append(rel)
    expected_retired=RETIRED_RUNTIME_ASSETS.intersection(preserved)
    assert_ok(set(retired)==expected_retired,f'intentional retirement mismatch: expected={sorted(expected_retired)}, actual={sorted(retired)}')
    assert_ok(not missing,'original source files missing: '+', '.join(missing))
    original_instructions=[x for x in preserved if x.startswith('instructions/')]
    instruction_count=sum(1 for p in (root/'instructions').rglob('*') if p.is_file())
    authority_files=[p for p in (root/'instructions').rglob('*.md') if any(x in p.parts for x in ('default','agents','profiles')) and p.name!='README.md' and 'roles' not in p.parts]
    assert_ok(all('codex-home:authority-v1' in p.read_text() for p in authority_files),'instruction authority contract missing')
    for folder in ('mcp/lib','mcp/container','mcp/scripts','scripts'):
        for p in (root/folder).glob('*.py'):ast.parse(p.read_text(),filename=str(p))
    report={'target':'custom Codex with 0.147.0 minimum compatibility and current model metadata','schema_used':'generate/schemas/config.schema.json',
        'schema_sha256':sha(schema_path),'schema_provenance':'schema embedded in uploaded codex-home archive; byte-identical pin, no upstream substitution',
        'active_configuration_files':len(configs),'main_config_lines':len((root/'home/config.toml').read_text().splitlines()),
        'toml_files_without_schema_metadata':len(toml_files),'runtime_root_settings':len(home),
        'configuration_schema_location':'build-time only: generate/schemas/',
        'schema_feature_keys':len(schema['properties']['features']['properties']),'active_feature_keys':len(expected),
        'feature_dispositions':{'removed':len(policy['removed']),'deprecated':len(policy['deprecated']),'legacy_aliases':len(policy['aliases']),'requirements_only':len(policy.get('requirements_only',[]))},
        'instruction_catalog_agent_references':len(refs),'original_instruction_files_unchanged':sum(x in same for x in original_instructions),'instruction_files':instruction_count,'authority_reviewed_templates':len(authority_files),
        'model_catalog_files':len(CANONICAL_CATALOG_PATHS),'model_catalog_members':catalogs,
        'model_catalog_metadata_source_version':CATALOG_METADATA_SOURCE_VERSION,
        'mcp_registrations':len(home['mcp_servers']),'podman_mcp_servers':len(mapping),'plugins_configured':len(home['plugins']),
        'hook_events':len(hooks['hooks']),'hook_handlers':handler_count,
        'original_files':len(preserved),'original_files_present':len(preserved)-len(missing)-len(retired),
        'original_files_accounted_for':len(preserved)-len(missing),'original_files_intentionally_removed':len(retired),
        'intentionally_removed_original_files':retired,'original_files_unchanged':len(same),
        'original_files_modified':changed,'missing_original_files':missing,'results':results,
        'requirements_check':'TOML + explicit nonrestrictive project-policy checks; separate from config.schema.json',
        'live_engine_tested':False,'live_podman_tested':False,
        'remaining':'Run target dependency, executable/resource, effective custom-client configuration and live MCP checks.'}
    if write:
        (root/'validation').mkdir(exist_ok=True)
        (root/'validation/static-report.json').write_text(json.dumps(report,indent=2)+'\n')
        (root/'validation/instruction-references.json').write_text(json.dumps(refs,indent=2)+'\n')
        coverage={'top_level':{k:('active' if k in home else 'optional, alternate, product-owned or compatibility-only; see generate/reports/config-coverage.json') for k in schema['properties']},
                  'features':{k:('active' if k in expected else 'removed' if k in policy['removed'] else 'deprecated' if k in policy['deprecated'] else 'requirements-only gate' if k in policy.get('requirements_only',[]) else 'legacy alias') for k in schema['properties']['features']['properties']}}
        (root/'validation/schema-coverage.json').write_text(json.dumps(coverage,indent=2)+'\n')
    return report

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--no-write',action='store_true');args=p.parse_args()
    try:
        r=validate(write=not args.no_write)
        print(f"PASS: {r['active_configuration_files']} config layers, {r['active_feature_keys']} active feature keys, {r['mcp_registrations']} MCP entries ({r['podman_mcp_servers']} Podman).")
        print(f"PASS: {r['instruction_files']} instruction files; {r['authority_reviewed_templates']} reviewed authority templates; {r['hook_events']} hook events / {r['hook_handlers']} handlers; {r['original_files_present']} originals retained + {r['original_files_intentionally_removed']} intentionally retired.")
        print('Schema SHA256: '+r['schema_sha256'])
        return 0
    except Exception as exc:
        print('VALIDATION FAILED: '+str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
