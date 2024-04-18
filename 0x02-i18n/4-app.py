#!/usr/bin/env python3
"""Module"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """set config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get the best matching language from the request or the forced locale."""
    # Check if 'locale' parameter is in the request query string
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        # Return the specified locale if it is supported
        return locale
    # Fallback to the best matching language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def home() -> str:
    """ display a HTML page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
