# Author: Jacianna Dockery
# Date: 11/11/2026
# File: place_manager.py
# Description: Retrieve places from the database.

from sqlalchemy.exc import SQLAlchemyError
from .place import Place
from .place_exceptions import PlaceException


class PlaceManager:

    @staticmethod
    def get_places():
        try:
            return Place.query.all()

        except SQLAlchemyError as error:
            raise PlaceException(
                "We couldn't load the places. Please try again later."
            ) from error
