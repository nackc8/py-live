from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["POST"])
def add():
    return "<p>Ta emot en URL, skapa och lagra en kort url, skicka tillbaka den korta urlen</p>"


@app.route("/gh6", methods=["DELETE"])
def remove():
    return "<p>Radera den korta URL:en <url>"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'
