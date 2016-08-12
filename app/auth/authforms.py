#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-11 14:43:02
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
# from flask import session
# from wtforms.csrf.session import SessionCSRF
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Email, Required, Length, EqualTo


# class AuthBaseForm(Form):
#     """配置csrf,之后的所有窗体都继承于此"""
#     class Meta(object):
#         """docstring for Meta"""
#         csrf = True
#         csrf_class = SessionCSRF
#         csrf_secret = 'auth csrf can not guess'

#         @property
#         def csrf_context(self):
#             return session


class LoginForm(Form):
    """docstring for FirstForm"""
    username = StringField('Username', validators=[Required(), Length(max=15)])
    password = PasswordField('Password', validators=[
                             Required(), Length(min=6, max=15)])
    rememberme = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegisterForm(Form):
    """docstring for RegistForm"""
    username = StringField('Username', validators=[Required(), Length(max=15)])
    email = StringField('Email', validators=[
                        Required(), Email(), Length(max=40)])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'repeatpsw', 'Password should be the same'), Length(max=15, min=6)])
    repeatpsw = PasswordField('Confirm Password', validators=[Required()])
    submit = SubmitField('Confirm')
