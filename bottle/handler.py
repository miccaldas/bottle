"""Module Docstring"""
import subprocess

import isort  # noqa: F401
from bottle import Bottle, request, template
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])

app = Bottle()


@app.route("form_page")
def handler():
    """"""

    return template("form_page.html", message="Please enter your name")


@app.route("form_page", method="GET")
def formhandler():

    first = request.form.get("first")
    last = request.form.get("last")

    message = f"Hello {first} {last}."

    return template("form_page.html", message=message)
