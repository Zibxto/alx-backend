#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, render_template
app: Flask = Flask(__name__)


@app.route('/', strict_slashes=False)
def home() -> str:
    """ display a HTML page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
