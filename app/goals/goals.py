# Author: Kelci Kempson
# Date: 11/12/26
# File: goals.py
# Description: the goals class

from extensions import db

class Goals(db.Model):
    __tablename__ = 'goals'

    goal_id = db.Column(db.Integer, primary_key=True)
    goal_type = db.Column(db.String(100), nullable=False)
    goal_amount = db.Column(db.Float, nullable=False)
    goal_timeframe = db.Column(db.String(50), nullable=False)

    def __init__(self, goal_id, goal_type, goal_amount, goal_timeframe):
        self.goal_id = goal_id
        self.goal_type = goal_type
        self.goal_amount = goal_amount
        self.goal_timeframe = goal_timeframe