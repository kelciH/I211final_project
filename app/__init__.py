# Author: Kelci Kempson
# Date: 11/11/26
# File: __init__.py
# Description: initializing the flask application
from extensions import db
from database import init_db
from flask import Flask


def create_app():
    app = Flask(__name__)

    # configure and initialize the SQLite database
    init_db(app)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    from .goals import bp as goals_bp
    app.register_blueprint(goals_bp)

    from .place import bp as placebp
    app.register_blueprint(placebp)

    from .categories import bp as categories_bp
    app.register_blueprint(categories_bp)

    # Handle database and page errors.
    from .place.place_exceptions import PlaceException
    from .goals.goals_exceptions import GoalException
    from .categories.category_exceptions import CategoryException

    @app.errorhandler(PlaceException)
    @app.errorhandler(GoalException)
    @app.errorhandler(CategoryException)
    @app.errorhandler(500)
    def handle_application_error(error):
        app.logger.error("Page loading failed: %s", error)
        return "We couldn't load this page. Please try again later.", 500

    # Register the homepage route from its separate file.
    from .routes import register_routes
    register_routes(app)

    return app
