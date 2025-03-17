from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hej världen!!!!</p>"


@app.route("/bye")
def bye_world():
    return "<p>Hej då världen!!!!</p>"
