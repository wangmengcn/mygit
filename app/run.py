#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-07 17:25:37
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask_mongoengine import MongoEngine
from flask.ext.login import LoginManager, UserMixin, login_user, logout_user, current_user
from flask.ext.pagedown import PageDown
from config import config
from oauth import OAuthSignIn


bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = MongoEngine()
pagedown = PageDown()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'index'


class User(db.Document):
    social_id = db.StringField(required=True)
    nickname = db.StringField(max_length=50)
    email = db.StringField(max_length=50)


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

app.config['OAUTH_CREDENTIALS'] = {
    'Github': {
        'id': 'bc4af5803f36aff59f99',
        'secret': 'ef60630f29923fe11556d8cf5644771029ade749'
    },
    'twitter': {
        'id': '3RzWQclolxWZIMq5LJqzRZPTl',
        'secret': 'm9TEd58DSEtRrZHpz2EjrV9AhsBRxKMo8m3kuIZj3zLwzwIimt'
    }
}


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    try:
        oauth = OAuthSignIn.getProvider(provider)
        return oauth.authorize()
    except Exception, e:
        raise e


@app.route('/callback/<provider>')
def oauth_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    oauth = OAuthSignIn.getProvider(provider)
    data = oauth.callback()
    print type(data)
    # social_id, username, email = oauth.callback()
    # if social_id is None:
    #     flash('Authentication failed.')
    #     return redirect(url_for('index'))
    # user = User.query.filter_by(social_id=social_id).first()
    # if not user:
    #     user = User(social_id=social_id, nickname=username, email=email)
    #     db.session.add(user)
    #     db.session.commit()
    # login_user(user, True)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
