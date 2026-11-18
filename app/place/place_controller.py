# Author: Jacianna Dockery
# Date: 11/11/2026
# File: place_controller.py
# Description: Load places and display the Places page.

from flask import render_template, abort, request
from jinja2 import TemplateError
from .place_manager import PlaceManager

# Place controller class
class PlaceController:

    @staticmethod
    def index():
        # display places matching search terms
        places = PlaceManager.get_places()

        try:
            # read the search text from the URL
            keywords = request.args.get("search", "").strip()

            places = PlaceManager.get_places(keywords)

            # send the records and search text to the template
            return render_template("places/index.html", places=places, search=keywords)

        except TemplateError:
            # send page-rendering errors to the centralized handler
            abort(500)
