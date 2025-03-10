import json
from pathlib import Path

json_path = Path(__file__).with_name("shopping.json")


class Cart:
    def __init__(self):
        self.content = {}

    def add(self, article, qty):
        self.content[article] = self.content.get(article, 0) + qty

    def load(self):
        with open(json_path, "r") as flp:
            content_json = flp.read()
        parsed = json.loads(content_json)
        self.content = parsed

    def save(self):
        content_json = json.dumps(self.content)
        with open(json_path, "w") as flp:
            flp.write(content_json)


# koekoeijeiijieijijejijie

cart1 = Cart()
cart1.load()
cart1.add("Banan", 1)
cart1.save()
