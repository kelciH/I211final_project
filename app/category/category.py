# Author: Jacianna Dockery
# Date: 11/11/2026
# File: category.py
# Description: Define the Category model for the finance tracker.

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from extensions import db


class Category(db.Model):
    __tablename__ = "categories"

    category_id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column(nullable=True)
    place_id: Mapped[int] = mapped_column(
        ForeignKey("place.place_id"),
        nullable=True
    )

    def __init__(self, category: str = "", place_id: int = None):
        self.category = category
        self.place_id = place_id

    def __repr__(self):
        return f"<Category {self.category}>"
