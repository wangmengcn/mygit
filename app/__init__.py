from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface
from flask.ext.login import LoginManager
from flask.ext.pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = MongoEngine()
pagedown = PageDown()
lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'auth.login'


def createApp(name):
    app = Flask(__name__)
    app.config.from_object(config[name])

    lm.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    app.session_interface = MongoEngineSessionInterface(db)
    pagedown.init_app(app)

    from .main import main as mainBluePrint
    app.register_blueprint(mainBluePrint)

    from .auth import auth as authBluePrint
    app.register_blueprint(authBluePrint)

    from .settings import setting as settingBluePrint
    app.register_blueprint(settingBluePrint, url_prefix='/setting')

    return app
