"""Finite ConfigToml path coverage, including structured alternative shapes."""
from pathlib import Path
import importlib.util
import json
import tomllib
ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT/'home/config.schema.json').read_text())
_sp = importlib.util.spec_from_file_location('validator', ROOT/'home/.hooks/schema_check.py')
v = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(v)

def resolve(node):
 while isinstance(node,dict) and '$ref' in node: node=SCHEMA['definitions'][node['$ref'].rsplit('/',1)[1]]
 return node

def field_paths(node,prefix=()):
 node=resolve(node)
 if not isinstance(node,dict): return set()
 result={prefix} if prefix else set()
 for branch in ['allOf','oneOf','anyOf']:
  for child in node.get(branch,[]): result |= field_paths(child,prefix)
 for k,child in node.get('properties',{}).items(): result |= field_paths(child,(*prefix,k))
 extra=node.get('additionalProperties')
 if isinstance(extra,dict): result |= field_paths(extra,(*prefix,'*'))
 if isinstance(node.get('items'),dict): result |= field_paths(node['items'],(*prefix,'[]'))
 return result

def present_paths(node,data,prefix=()):
 node=resolve(node)
 if not isinstance(node,dict): return set()
 result={prefix} if prefix else set()
 for branch in ['allOf','oneOf','anyOf']:
  for child in node.get(branch,[]):
   try: v.validate(SCHEMA,data,child)
   except v.SchemaError: continue
   result |= present_paths(child,data,prefix)
 if isinstance(data,dict):
  for k,x in data.items():
   if k in node.get('properties',{}): result |= present_paths(node['properties'][k],x,(*prefix,k))
   elif isinstance(node.get('additionalProperties'),dict): result |= present_paths(node['additionalProperties'],x,(*prefix,'*'))
 if isinstance(data,list) and isinstance(node.get('items'),dict):
  for x in data: result |= present_paths(node['items'],x,(*prefix,'[]'))
 return result
