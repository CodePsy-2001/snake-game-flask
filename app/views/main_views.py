from flask import Blueprint
from flask import g, session
from flask.templating import render_template

from app import db
from app.models import User

bp = Blueprint('main', __name__, url_prefix='/')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/', methods=['GET'])
# @logincheck
def index():
    return render_template('main/index.html')