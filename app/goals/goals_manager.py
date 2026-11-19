# Author: Kelci Kempson
# Date: 11/12/26
# File: goals_manager.py
# Description: managing the data
from flask import abort
from sqlalchemy.exc import SQLAlchemyError

from extensions import db
from sqlalchemy import select
from .goals import (Goals)
from .goals_exceptions import GoalNotFoundException

class GoalsManager:
    @staticmethod
    def get_goals() -> list:
        try:
            stmt = select(Goals)
            goals = db.session.scalars(stmt).all()
            return goals

        except Exception as e:
            raise GoalNotFoundException(e)

    @staticmethod
    def get_goals_by_amount(min_amount=None, max_amount=None) -> list:
        try:
            stmt = select(Goals)

            if min_amount is not None:
                stmt = stmt.where(Goals.goal_amount >= min_amount)

            if max_amount is not None:
                stmt = stmt.where(Goals.goal_amount <= max_amount)

            goals = db.session.scalars(stmt).all()

            if not goals:
                raise GoalNotFoundException(
                    "No goals found within the specified amount range."
                )

            return goals

        except Exception as e:
            return GoalsManager.handle_exceptions(e)

#method for exceptions
    @staticmethod
    def handle_exceptions(e):
        db.session.rollback()
        # Call abort from flask here. This will raise an HTTPException
        # and trigger the centralized error handlers in app/__init__.py
        if isinstance(e, GoalNotFoundException):
            abort(404, description=str(e))
        elif isinstance(e, SQLAlchemyError):
            # Database-specific errors are handled as internal server errors
            abort(500, description=f"A database error occurred: {str(e)}")
        else:
            # all other exceptions are treated as internal server errors
            abort(500, description=str(e))