from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


def generate_str_with_breaklines(**kwargs):
    str_ = ""
    for k, v in kwargs.items():
        str_ += f"'{k}': '{v}' <br>"
    return str_


@app.route("/myip", methods=["GET", "POST"])
@limiter.limit("10/minute")
def myip():
    return generate_str_with_breaklines(
        request_method=request.method,
        remote_address=get_remote_address(),
        os_pid=os.getpid(),
        request_remote=request.environ["REMOTE_ADDR"],
        request_forward=request.environ['HTTP_X_FORWARDED_FOR']
    )
