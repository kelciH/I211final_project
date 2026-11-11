# Author: Kelci Kempson
# Date: 11/11/26
# File: __init__.py
# Description: initializing the flask application
from flask import Flask, render_template
from datetime import datetime
from extensions import db
from database import init_db


def create_app():
    app = Flask(__name__)

    # configure and initialize the SQLite database
    init_db(app)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    from .goals import bp as goals_bp
    app.register_blueprint(goals_bp)

    # Application error handling
    @app.errorhandler(401)
    def unauthorized_error(error):
        return render_template('errors/401.html', error=error), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', error=error), 404

    @app.errorhandler(409)
    def conflict_error(error):
        return render_template('errors/409.html', error=error), 409

    @app.route('/')
    def index():
        return render_template('index.html', year=datetime.now().year)

    return app
