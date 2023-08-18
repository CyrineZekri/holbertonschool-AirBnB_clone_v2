#!/usr/bin/python3
"""
Web app with two routes
"""
from flask import Flask
app = Flask("__name_")

strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def page_1():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug="true")
