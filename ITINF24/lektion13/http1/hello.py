from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hej världen!</p>"

flask.add_route(hello_world, "/")

