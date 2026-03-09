from flask import Flask, request

app = Flask(__name__)

next_unique_int = 1
urls = dict()


@app.route("/", methods=["POST"])
def add():
    global next_unique_int

    json = request.get_json()
    original_url = json["url"]

    short_url = str(next_unique_int)
    next_unique_int += 1

    urls[short_url] = original_url
    # TODO: Use more characters than 0-9 for short urls
    return short_url


@app.route("/<shorturl>", methods=["DELETE"])
def remove(shorturl):
    return f"<p>Radera den korta URL:en {shorturl}"
