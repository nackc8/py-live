import json
from pathlib import Path

json_path = Path(__file__).with_name("lsblk-j.json")

with open(json_path) as filehandle:
    json_content = filehandle.read()

json_loaded = json.loads(json_content)

print("keys:", json_loaded.keys())

for el in json_loaded["blockdevices"]:
    print(el["name"])
