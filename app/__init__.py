from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask_mongoengine import MongoEngine
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from config import config


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = MongoEngine()
pagedown = PageDown()
lm = LoginManager()
lm.login_view = 'index'


def createApp(name):
    app = Flask(__name__)
    app.config.from_object(config[name])

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    pagedown.init_app(app)
    lm.init_app(app)

    from .main import main as mainBluePrint
    app.register_blueprint(mainBluePrint)

    from .auth import auth as authBluePrint
    app.register_blueprint(authBluePrint)

    return app
