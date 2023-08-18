#!/usr/bin/python3
"""
Another route with dynamic parameter and default value
"""
from flask import Flask
app = Flask("__name__")
strict_slashes = False


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def page_1():
    return "HBNB"


@app.route("/c/<text>")
def page_2(text):
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/")
@app.route("/python/<text>")
def page_3(text="is cool"):
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
