# Author: Jacianna Dockery
# Date: 11/11/2026
# File: database.py
# Description: the connection to the tracker database.

import os


def init_db(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    database_path = os.path.join(basedir, "tracker.db")

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
