
# Author: Jacianna Dockery
# Date: 11/11/2026
# File: __init__.py
# Description: place blueprint

from flask import Blueprint

bp = Blueprint(
    "place",
    __name__,
    url_prefix="/places",
    template_folder="templates",
    static_folder="static"
)

from . import routes