import os

from flask import Flask, g
from flask_httpauth import HTTPTokenAuth

app = Flask(__name__)
auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    if token == os.getenv("USER_TOKEN"):
        return token


@app.route("/")
@auth.login_required
def index():
    return "Hello, Devops challenger!"


if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
