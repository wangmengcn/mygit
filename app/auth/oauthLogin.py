#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:41:30
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from flask import redirect, url_for, request, render_template
from flask.ext.login import login_user, logout_user, current_user

from . import auth
from .oauth import OAuthSignIn
from ..models import User


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.main_index'))


@auth.route('/authorize/<provider>')
def oauth_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    try:
        oauth = OAuthSignIn.getProvider(provider)
        return oauth.authorize()
    except Exception, e:
        raise e


@auth.route('/callback/Github')
def oauth_callback():
    code = request.args.get('code', 1, type=str)
    oauth = OAuthSignIn.getProvider('Github')
    logininfo = oauth.callback(code)
    flag = User.objects(username=logininfo['login'])
    user = User(username=logininfo['login'], avatar_url=logininfo[
        'avatar_url'], html_url=logininfo['html_url'])
    if len(flag) == 0:
        user.save()
    loginuser = User.objects(username=logininfo['login'])[0]
    login_user(loginuser)
    return render_template('index.html')


@auth.route('/callback/BattleNet')
def Battlenet_oauth_callback():
    code = request.args.get('code', 1, type=str)
    oauth = OAuthSignIn.getProvider('BattleNet')
    logininfo = oauth.callback(code)
    print logininfo
    flag = User.objects(username=logininfo['battletag'])
    user = User(username=logininfo['battletag'],
                html_url=logininfo['id'])
    if len(flag) == 0:
        user.save()
    loginuser = User.objects(username=logininfo['battletag'])[0]
    login_user(loginuser)
    return render_template('index.html')
