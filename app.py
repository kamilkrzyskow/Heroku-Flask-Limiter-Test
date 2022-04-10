from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


@app.route("/myip")
@limiter.limit("10/minute")
def myip():
    return f"GET {get_remote_address()}"


@app.route("/myip", methods="POST")
@limiter.limit("10/minute")
def myip():
    return f"POST {get_remote_address()}"
