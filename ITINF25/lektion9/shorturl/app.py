from flask import Flask, request

app = Flask(__name__)

next_unique_int = 1
urls = dict()


@app.route("/", methods=["POST"])
def add():
    json = request.get_json()
    original_url = json["url"]

    short_url = str(next_unique_int)
    global next_unique_int
    next_unique_int += 1

    urls[original_url] = "Sett!"
    print(urls)
    return "<p>Ta emot en URL, skapa och lagra en kort url, skicka tillbaka den korta urlen</p>"


@app.route("/<shorturl>", methods=["DELETE"])
def remove(shorturl):
    return f"<p>Radera den korta URL:en {shorturl}"
