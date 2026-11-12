# Author: Jacianna Dockery
# Date: 11/11/2026
# File: routes.py
# Description: Define the places route

from . import bp
from .place_controller import PlaceController

@bp.route("/")
def index():
    return PlaceController.index()
