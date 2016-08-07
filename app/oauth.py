#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-07 19:45:15
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from rauth import OAuth1Service, OAuth2Service
from flask import current_app, url_for, request, redirect, session


class OAuthSignIn(object):
    """docstring for OAuthSignIn"""
    providers = None

    def __init__(self, providerName):
        self.providerName = providerName
        credentials = current_app.config['OAUTH_CREDENTIALS'][providerName]
        self.consumerId = credentials['id']
        self.consumerSecret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def getCallbackURL(self):
        pass

    @classmethod
    def getProvider(self, providerName):
        if self.providers is None:
            self.providers = {}
            for providerClass in self.__subclasses__():
                provider = providerClass()
                self.providers[provider.providerName] = provider
        return self.providers[providerName]


class GithubSigIn(OAuthSignIn):
    """docstring for GithubSigIn"""

    def __init__(self):
        super(GithubSigIn, self).__init__('Github')
        self.service = OAuth2Service(
            name='Github',
            client_id=self.consumerId,
            client_secret=self.consumerSecret,
            authorize_url='https://github.com/login/oauth/authorize',
            access_token_url='https://github.com/login/oauth/access_token',
        )

    def authorize(self):
        return redirect(self.service.get_authorize_url(
            scope='user',
            response_type='code',
            redirect_url=self.getCallbackURL()))

    def callback(self):
        if 'code' not in request.args:
            return None, None, None
        oauthSession = self.service.get_auth_session(
            data=dict(code=request.args['code'],
                      redirect_url=self.getCallbackURL(),
                      scope='public_repo'))
        print type(oauthSession)
        print oauthSession
        print "!!!!"
        # me = oauthSession.get('user').json()
        # flash('Logged in as ' + me['name'])
        return redirect(url_for('index'))
