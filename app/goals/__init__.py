# Author: Kelci Kempson
# Date: 11/11/26
# File: __init__.py
# Description: initilazing bp
from flask import Blueprint, render_template

bp = Blueprint('goals', __name__, url_prefix='/goals',
               static_folder='static', template_folder='templates')

@bp.route('/')
def goals():
    return render_template('goals.html')