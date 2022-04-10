from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


@app.route("/myip", methods=["GET", "POST"])
@limiter.limit("10/minute")
def myip():
    return f"{request.method} {get_remote_address()}"
