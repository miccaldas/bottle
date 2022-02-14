"""Module Docstring"""
import subprocess

import isort  # noqa: F401
from bottle import Bottle, template
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])
app = Bottle()


@app.route("/test")
def homepage():
    """Home page"""

    info = {"title": "Welcome Home!", "content": "Hello World"}
    print("TESTE")
    return template("simple.tpl", info)


if __name__ == "__main__":
    app.run()
