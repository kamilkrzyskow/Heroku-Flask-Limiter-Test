from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


@app.route("/slow")
@limiter.limit("1 per day")
def slow():
    return ":("


@app.route("/medium")
@limiter.limit("1/second", override_defaults=False)
def medium():
    return ":|"


@app.route("/fast")
def fast():
    return ":)"


@app.route("/ping")
@limiter.exempt
def ping():
    return "PONG"


@app.route("/myip")
@limiter.limit("1/minute")
def myip():
    return get_remote_address()
