import json
from pathlib import Path

json_path = Path(__file__).with_name("shopping.json")


class Cart:
    def __init__(self):
        self.content = {}

    def add(self, article, qty):
        self.content[article] = self.content.get(article, 0) + qty

    def save(self):
        content_json = json.dumps(self.content)
        with open(json_path, 'w') as flp:
            flp.
