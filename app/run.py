#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-07 17:25:37
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Flask, render_template, redirect, url_for, flash, request
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
logininfo = None


class User(UserMixin, db.Document):
    username = db.StringField(required=True)
    avatar_url = db.StringField(max_length=100)
    html_url = db.StringField(max_length=100)

    @property
    def is_active(self):
        return True

    @property
    def get_id(self):
        return self.username

    @property
    def is_authenticated(self):
        return self.authenticated

    @property
    def is_anonymous(self):
        # False as we do not support annonymity
        return False

    @staticmethod
    def query(username):
        result = User.objects(username=username)
        print type(result)
        # value = User(username=result['username'], avatar_url=result[
        #              'avatar_url'], html_url=result['html_url'])
        return None



app = Flask(__name__)
app.config.from_object(config['defualt'])
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

bootstrap.init_app(app)
mail.init_app(app)
moment.init_app(app)
db.init_app(app)
pagedown.init_app(app)


# @login_manager.user_loader
# def load_user(username):
#     return User.query(username)


@app.route('/')
def index(data=None):
    return render_template('index.html',data=data)


@app.route('/logout')
def logout():
    return redirect(url_for('index',data=None))


@app.route('/authorize/<provider>')
def oauth_authorize(provider):
    try:
        oauth = OAuthSignIn.getProvider(provider)
        return oauth.authorize()
    except Exception, e:
        raise e


@app.route('/callback/Github')
def oauth_callback():
    code = request.args.get('code', 1, type=str)
    print code
    oauth = OAuthSignIn.getProvider('Github')
    logininfo = oauth.callback(code)
    user = User(username=logininfo['login'], avatar_url=logininfo[
                'avatar_url'], html_url=logininfo['html_url'])
    user.save()
    return render_template('index.html',data=logininfo)


if __name__ == '__main__':
    app.run()
