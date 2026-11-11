# Author: Kelci Kempson
# Date: 11/11/26
# File: database.py
# Description: database

import os

def init_db(app):
    basedir = os.path.abspath(os.path.dirname(__file__))
    connection_string = ('sqlite:///' + os.path.join(basedir, 'kungfupanda.db'))

    app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
