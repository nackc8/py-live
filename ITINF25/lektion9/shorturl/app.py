from flask import Flask, Request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def add():
    return "<p>Ta emot en URL, skapa och lagra en kort url, skicka tillbaka den korta urlen</p>"


@app.route("/<shorturl>", methods=["DELETE"])
def remove(shorturl):
    return f"<p>Radera den korta URL:en {shorturl}"
