#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-07 17:26:25
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """docstring for Config"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MYGIT_MAIL_SUBJECT_PREFIX = '[mygit]'
    MYGIT_MAIL_SENDER = 'mygit Admin <eclipse_sv@163.com>'
    MYGIT_ADMIN = os.environ.get('MYGIT_ADMIN')
    MYGIT_POSTS_PER_PAGE = 20
    MYGIT_FOLLOWERS_PER_PAGE = 50
    MYGIT_COMMENTS_PER_PAGE = 30
    MYGIT_SLOW_DB_QUERY_TIME = 0.5

    @staticmethod
    def init_app(app):
        pass


class Devlopment(Config):
    """docstring for Devlopment"""
    MONGODB_SETTINGS = {
        'db': 'mygit',
        'host': 'localhost',
        'port': 27017
    }
    MYGIT_REDIS_HOST = 'localhost'
    MYGIT_REDIS_PORT = 6379


config = {
    'defualt': Devlopment
}
