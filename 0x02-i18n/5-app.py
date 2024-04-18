#!/usr/bin/env python3
"""Module"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """set config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """Return a user dictionary based on the user ID from the request.

    Returns:
        dict or None: A user dictionary if the user
                      ID exists in the users dictionary,
                      otherwise None.
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    user_id = int(user_id)
    return users.get(user_id)


@app.before_request
def before_request():
    """Set user as a global in the application context."""
    g.user = get_user()


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
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
