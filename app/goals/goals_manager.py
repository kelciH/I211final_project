# Author: Kelci Kempson
# Date: 11/12/26
# File: goals_manager.py
# Description: managing the data

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

            print("Database:", db.engine.url)

            print("Goals retrieved:", goals)
            print("Number of goals:", len(goals))

            return goals

        except Exception as e:
            raise GoalNotFoundException(e)
