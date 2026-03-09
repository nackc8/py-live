import db
from flask import Flask, jsonify, redirect, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def add():
    json = request.get_json()
    original_url = json["url"]

    url = db.Url(original=original_url)
    url.save()

    url_short = str(url.id)

    return jsonify(
        {
            "url_short": url_short,
            "original_url": original_url,
        }
    )


@app.route("/<short_url>", methods=["DELETE"])
def remove(short_url):
    print(f"remove {short_url}")
    short_url = db.Url.get_by_id(short_url)
    short_url.delete_instance()

    return ("", 204)


@app.route("/<short_url>", methods=["GET"])
def redirect_to_original_url(short_url):
    short_url = db.Url.get_by_id(short_url)
    original_url = short_url.original
    return redirect(original_url)
