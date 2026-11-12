# Author: Jacianna Dockery
# Date: 11/11/2026
# File: __init__.py

# Description: initilazing bp
from flask import Blueprint, render_template
from .category_manager import CategoryManager

bp = Blueprint('categories', __name__, url_prefix='/categories',
               static_folder='static', template_folder='templates')

@bp.route('/')
def categories():
    categories =  CategoryManager.get_categories()

    return render_template('category.html', categories=categories)