# Author: Jacianna Dockery
# Date: 11/18/2026
# File: routes.py
# Description: routes for the Categories page

from . import bp
from .category_controller import CategoryController


@bp.route("/")
def categories():
   # send requests for the Categories page to its controller.
    return CategoryController.index()