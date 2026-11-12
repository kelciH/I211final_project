# Author: Jacianna Dockery
# Date: 11/11/2026
# File: category_manager.py
# Description: Retrieve categories from the database.
from sqlalchemy.exc import SQLAlchemyError
from .category import Category
from .category_exceptions import CategoryException


class CategoryManager:

    @staticmethod
    def get_categories():
        try:
            return Category.query.all()

        except SQLAlchemyError as error:
            raise CategoryException(
                "We couldn't load the categories. Please try again later."
            ) from error
