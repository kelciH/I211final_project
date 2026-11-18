# Author: Jacianna Dockery
# Date: 11/11/2026
# File: category_manager.py
# Description: Retrieve categories from the database.
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from .category import Category
from .category_exceptions import CategoryException


class CategoryManager:

    @staticmethod
    def get_categories():
        try:
            # Load the related places along with the categories
            stmt = select(Category).options(selectinload(Category.place))

            return db.session.scalars(stmt).all()

        except SQLAlchemyError as error:
            raise CategoryException(
                "We couldn't load the categories. Please try again later."
            ) from error
