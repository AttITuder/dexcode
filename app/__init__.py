from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_pagedown import PageDown
from flask_moment import Moment
from flask_login import LoginManager
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.index'
pagedown = PageDown()
moment = Moment()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
