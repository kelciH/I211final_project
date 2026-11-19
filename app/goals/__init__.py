# Author: Kelci Kempson
# Date: 11/11/26
# File: __init__.py
# Description: initilazing bp
from flask import Blueprint, render_template, request

from extensions import db
from .goals import Goals
from .goals_manager import GoalsManager

bp = Blueprint('goals', __name__, url_prefix='/goals',
               static_folder='static', template_folder='templates')

@bp.route('/')
def goals():

    min_amount = request.args.get('min_amount', type=float)
    max_amount = request.args.get('max_amount', type=float)

    goals_query = db.session.query(Goals)

    if min_amount is not None:
        goals_query = goals_query.filter(Goals.goal_amount >= min_amount)

    if max_amount is not None:
        goals_query = goals_query.filter(Goals.goal_amount <= max_amount)

    goals = goals_query.all()

    return render_template('goals.html', goals=goals)