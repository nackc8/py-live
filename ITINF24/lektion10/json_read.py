import json

json_content = '{ "greeting": "hello", "year": 123  }'

json_loaded = json.loads(json_content)

print(type(json_loaded))

print(json_loaded["greeting"])
print(type(json_loaded["greeting"]))

print(json_loaded["year"])
print(type(json_loaded["year"]))
