from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def add():
    return "<p>Ta emot en URL, skapa och lagra en kort url, skicka tillbaka den korta urlen</p>"
