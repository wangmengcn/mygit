#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:35:21
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import os
from flask import render_template, redirect, url_for, g
from flask.ext.login import login_required, current_user

from . import main
from mainForms import ProfileForm, PostForm
from ..models import Profile


@main.before_app_request
def before_request():
    pass


@main.route('/')
def main_index():
    return render_template('index.html')


@main.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        user = current_user.id
        userProfile = Profile(location=form.location.data,
                              job=form.job.data, position=form.position.data, filed=form.filed.data)
        if Profile.objects(user=user).first() is None:
            userProfile.save()
        return render_template('index.html')
    return render_template('profile.html', form=form)


@main.route('/setting')
@login_required
def userSetting():
    pass


@main.route('/post')
@login_required
def posts():
    form = PostForm()
    if form.validate_on_submit():
        return redirect(url_for('main.main_index'))
    return render_template('posts.html', form=form)
