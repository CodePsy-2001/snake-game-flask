from flask import Blueprint, Response
from flask import g, request, session
from flask.templating import render_template
from urllib import parse

from app import db
from app.models import User, Scoreboard
from datetime import datetime

bp = Blueprint('rank', __name__, url_prefix='/')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)


@bp.route('/rank/', methods=['GET', 'POST'])
def rank():
    if request.method == 'GET':
        score_list = Scoreboard.query.order_by(Scoreboard.highscore.desc())
        if not g.user:
            return render_template('rank/rank.html', score_list=score_list) # TODO: 로그인 한것과 안한것 다르게
        return render_template('rank/rank.html', score_list=score_list, username=g.user.username,
            highscore=Scoreboard.query.filter_by(username=g.user.username).first().highscore)

    elif request.method == 'POST':
        username=parse.unquote(request.headers['username'])
        highscore=int(request.headers['highscore'])
        print("POST 요청:", username, highscore)

        pre = Scoreboard.query.filter_by(username=username).first()
        if pre:
            if highscore > pre.highscore:
                pre.highscore = highscore
                pre.create_date = datetime.now()
                db.session.commit()
        else:
            score = Scoreboard(username=username, highscore=highscore, create_date=datetime.now())
            db.session.add(score)
            db.session.commit()

        return Response(status=200)