from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)

    # ORM - 손대지 마시오
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # Blueprint
    from .views import main_views, auth_views, game_views, rank_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(game_views.bp)
    app.register_blueprint(rank_views.bp)

    return app