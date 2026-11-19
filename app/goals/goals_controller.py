# Author: Kelci Kempson
# Date: 11/12/26
# File: goals_controller.py
# Description: controller goals

from flask import render_template, request
from .goals_manager import GoalsManager


class GoalsController:
#getting all information to index
    @staticmethod
    def index():

        min_amount = request.args.get('min_amount', type=float)
        max_amount = request.args.get('max_amount', type=float)

        if min_amount is not None or max_amount is not None:
            result = GoalsManager.get_goals_by_amount(
                min_amount=min_amount,
                max_amount=max_amount
            )
        else:
            result = GoalsManager.get_goals()

        return render_template('goals.html', goals=result)