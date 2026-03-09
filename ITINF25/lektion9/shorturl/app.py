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
    print(f"add {original_url} -> {short_url}")
    print("urls", urls)
    return short_url


@app.route("/<short_url>", methods=["DELETE"])
def remove(short_url):
    print(f"remove {short_url}")
    print("urls", urls)
    urls.pop(short_url)
    return ""
