#!/usr/bin/env python3

"""
Force locale with URL parameter
"""

from flask import Flask, render_template, request
from Flask_babel import babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Make configurations
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE ="UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """
    Get locale
    """
    locale = request.args.get("locale")
    if locale:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    return string
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
