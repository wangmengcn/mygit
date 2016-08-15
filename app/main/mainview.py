#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:35:21
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from flask import render_template
from flask.ext.login import login_required, current_user

from . import main
from mainForms import ProfileForm


@main.route('/')
def main_index():
    return render_template('index.html')


@main.route('/profile')
# @login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        user = current_user
        userProfile = Profile(location=form.location.data,
                              job=form.job.data, position=form.position.data, filed=form.filed.data)
        if Profile.objects(user=user).first() is not None:
            userProfile.save()
        return render_template('profile.html')
    return render_template('profile.html', form=form)
