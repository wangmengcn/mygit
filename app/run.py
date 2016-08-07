#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-07 17:25:37
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

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
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    return app

app = creat_app('defualt')

if __name__ == '__main__':
    app.run()