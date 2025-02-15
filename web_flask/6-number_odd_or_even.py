#!/usr/bin/python3
"""
rendering template with conditions
"""
from flask import Flask, render_template


app = Flask(__name__)

strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c(text):
    a = text.replace("_", " ")
    return f"C {a}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def python(text='is cool'):
    b = text.replace("_", " ")
    return f"Python {b}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    if type(n) is int:
        return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
