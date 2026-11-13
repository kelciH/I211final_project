# Author: Jacianna Dockery
# Date: 11/11/2026
# File: place_controller.py
# Description: Load places and display the Places page.

from flask import render_template, abort
from jinja2 import TemplateError
from .place_manager import PlaceManager


class PlaceController:

    @staticmethod
    def index():
        places = PlaceManager.get_places()

        try:
            return render_template("places/index.html", places=places)

        except TemplateError:
            abort(500)
