from flask import Flask

app = Flask(__name__)

# Kör med: flask --app vars --debug run


@app.route("/")
def hello_world():
    return "<p>Hej världen!!!!</p>"


@app.route("/bye")
def bye_world():
    return "<p>Hej då världen!!!!</p>"
