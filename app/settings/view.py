#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-18 15:35:41
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from flask import redirect, render_template, url_for, flash
from flask.ext.login import current_user, logout_user, login_required
from . import setting
from settingForm import ResetEmailForm, ResetPasswordForm


@setting.route('/reset_password', methods=['GET', 'POST'])
@login_required
def password_reset_request():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if form.oldpsw.data == current_user.password:
            current_user.password = form.newpsw.data
            current_user.save()
            logout_user()
            flash('Password changed! Please Login in')
            return render_template('index.html')
        flash('Invalid password.')
    return render_template('setting/resetpsw.html', form=form)


@setting.route('/reset_email', methods=['GET', 'POST'])
@login_required
def email_reset_request():
    form = ResetEmailForm()
    if form.validate_on_submit():
        if form.oldemil.data == current_user.email:
            current_user.email = form.newemail.data
            current_user.save()
            flash('Email changed!')
            return redirect(url_for('main.main_index'))
        flash('Invalid email')
    return render_template('setting/resetemil.html', form=form)
