import json

json_content = '{ "greeting": "hello"  }'

json_loaded = json.loads(json_content)

print(type(json_loaded))

print(json_loaded)
