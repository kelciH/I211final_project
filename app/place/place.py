# Author: Jacianna Dockery
# Date: 11/11/2026
# File: place.py
# Description: define the Place model for the finance tracker.


from sqlalchemy.orm import Mapped, mapped_column, relationship
from extensions import db


class Place(db.Model):
    __tablename__ = "place"

    place_id: Mapped[int] = mapped_column(primary_key=True)
    place: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)

    # access the categories associated with this place
    categories: Mapped[list["Category"]] = relationship("Category", back_populates="place")

    def __init__(self, place: str = "", description: str = ""):
        self.place = place
        self.description = description


    def __repr__(self):
        return f"<Place {self.place}>"
