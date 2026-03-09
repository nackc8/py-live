from flask import Flask, request

app = Flask(__name__)

next_unique_int = 1
urls = dict()


@app.route("/", methods=["POST"])
def add():
    json = request.get_json()
    url = json["url"]

    urls[url] = "Sett!"
    print(urls)
    return "<p>Ta emot en URL, skapa och lagra en kort url, skicka tillbaka den korta urlen</p>"


@app.route("/<shorturl>", methods=["DELETE"])
def remove(shorturl):
    return f"<p>Radera den korta URL:en {shorturl}"
