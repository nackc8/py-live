import db
from flask import Flask, redirect, request

app = Flask(__name__)

next_unique_int = 1


@app.route("/", methods=["POST"])
def add():
    global next_unique_int

    json = request.get_json()
    original_url = json["url"]

    short_url = str(next_unique_int)
    next_unique_int += 1

    url_map = db.Url(short=short_url, original=original_url)
    url_map.save()

    # TODO: Use more characters than 0-9 for short urls
    print(f"add {original_url} -> {short_url}")
    return short_url


@app.route("/<short_url>", methods=["DELETE"])
def remove(short_url):
    print(f"remove {short_url}")
    short_url = db.Url().select().where(db.Url.short == short_url)
    short_url.delete_instance()

    return ("", 204)


@app.route("/<short_url>", methods=["GET"])
def redirect_to_original_url(short_url):
    short_url = db.Url().select().where(db.Url.short == short_url)
    original_url = short_url.original
    print(f"redirect {short_url} -> {original_url}")
    return redirect(original_url)
