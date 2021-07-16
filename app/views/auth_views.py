from flask import Blueprint
from flask import g, request, session, redirect, flash, url_for
from flask.templating import render_template
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from app import db
from app.models import User
from ..forms import UserCreateForm, UserLoginForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(user_id)



# TODO: 
@bp.route('/', methods=['GET'])
def auth():
    return redirect(url_for('main.index'))


@bp.route('/signup/', methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        # 기존 유저 있는지 검증 - 이메일 기준
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            user = User (
                username=form.username.data,
                password=generate_password_hash(form.password1.data),
                email=form.email.data,
                create_date=datetime.now()
                )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            flash('이미 존재하는 사용자입니다.')

    return render_template('auth/signup.html', form=form)


@bp.route('/login/', methods=['GET', 'POST'])
def login():
    form = UserLoginForm()
    if request.method == 'GET':
        if g.user:
            flash('이미 로그인되어 있습니다!')
            return redirect(url_for('game.game')) # game으로 GET 요청 보냄
        return render_template('auth/login.html', form=form)

    elif request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data): # DB와 비교하기 위해 똑같이 암호화
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear() # 이미 있는 세션이 있다면 치우고
            session['user_id'] = user.id # 세션 user_id key값에, 호출된 user의 id 고유키를 집어넣음 
            return redirect(url_for('main.index')) # game으로 GET 요청 보냄
        flash(error)
    return render_template('auth/login.html', form=form)


@bp.route('/logout/')
def logout():
    session.clear()
    return redirect(url_for('main.index'))

