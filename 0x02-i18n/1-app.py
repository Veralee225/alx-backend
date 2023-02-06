#!/usr/bin/env python3

"""
1. Basic Flask Apps
"""

from flask import Flask, render_templates, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class config:
    """
    Config class
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_LOCALE = "UTC"


app.config.from_object(config)


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    return string
    """
    return render_templates('1-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
