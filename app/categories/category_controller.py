# Author: Jacianna Dockery
# Date: 11/18/2026
# File: category_controller.py
# Description: controller for the Categories page

from flask import render_template, abort
from jinja2 import TemplateError
from .category_manager import CategoryManager

class CategoryController:

    @staticmethod
    def index():
     # load the Categories with their related places
        try:
            categories = CategoryManager.get_categories()

            return render_template('category.html', categories=categories)


        except TemplateError as e:
            # Send rendering errors to the centralized handler.
            abort(500)
