# Author: Jacianna Dockery
# Date: 11/11/2026
# File: __init__.py

from flask import Blueprint

# Create the Categories blueprint.
bp = Blueprint(
    "categories",
    __name__,
    url_prefix="/categories",
    static_folder="static",
    template_folder="templates"
)

# Load routes after the blueprint has been created.
from . import routes
