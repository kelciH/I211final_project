# Author: Jacianna Dockery
# Date: 11/18/2026
# File: routes.py
# Description:

from flask import render_template
from datetime import datetime

# register the application's routes
def register_routes(app):

# display the finance tracker homepage
    @app.route("/")
    def index():

        return render_template("index.html", year=datetime.now().year)
