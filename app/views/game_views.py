from flask import Blueprint
from flask import redirect, flash, g, request, session
from flask.templating import render_template

from app.models import User, Scoreboard

bp = Blueprint('game', __name__, url_prefix='/')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/game/', methods=['GET'])
def game():
    if not g.user: # 로그인 상태가 아니면
        data = {
            'username': 'guest',
            'highscore': 0,
            }
    else:
        user = Scoreboard.query.filter_by(username=g.user.username).first()
        if not user: # 로그인은 되어있는데 기존 최고기록이 없으면
            data = {
                'username': g.user.username,
                'highscore': 0,
                }
        else:
            data = {
                'username': g.user.username,
                'highscore': user.highscore,
                }
    return render_template('game/game.html', data=data)