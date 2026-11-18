# Author: Jacianna Dockery
# Date: 11/11/2026
# File: place_manager.py
# Description: Retrieve places from the database.

from sqlalchemy import select, or_
from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from .place import Place
from .place_exceptions import PlaceException


class PlaceManager:


    @staticmethod
    def get_places(keywords = ""):
        try:
            # Create a query that selects all places
            stmt = select(Place)

            # split the search text into individual keywords
            search_terms = keywords.split()

            # Match each word against the place name
            conditions = []
            for word in search_terms:
                conditions.append(Place.place.like(f"%{word}%"))
                conditions.append(Place.description.like(f"%{word}%"))

            # Include places that match any of the conditions
            if conditions:
                stmt = stmt.where(or_(*conditions))

            # execute the query
            return db.session.scalars(stmt).all()

        except SQLAlchemyError as error:
            # friendly message
            raise PlaceException(
                "We couldn't load the places. Please try again later."
            ) from error


