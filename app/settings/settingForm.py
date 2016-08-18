#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-18 15:36:12
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, Required, Length, EqualTo


class ResetPasswordForm(Form):
    """docstring for ResetPasswordForm"""
    oldpsw = PasswordField('Old Password', validators=[
                           Required(), Length(max=15, min=6)])
    newpsw = PasswordField('New Password', validators=[
                           Required(), Length(max=15, min=6), EqualTo('confrimpsw')])
    confrimpsw = PasswordField('Confrim password', validators=[Required()])
    submit = SubmitField('Change Password')


class ResetEmailForm(Form):
    """docstring for ResetEmailForm"""
    oldemil = StringField("Old Email", validators=[
                          Required(), Length(max=40), Email()])
    newemail = StringField("New Email", validators=[
                           Required(), Length(max=40), Email()])
    submit = SubmitField("Change Email")
