#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:35:21
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import os
from datetime import datetime
from flask import render_template, redirect, url_for, g, request
from flask.ext.login import login_required, current_user

from . import main
from mainForms import ProfileForm, PostForm
from ..models import Profile, Post


@main.before_app_request
def before_request():
    pass


@main.route('/')
def main_index():
    if current_user.is_authenticated:
        posts = []
        for post in Post.objects(user=current_user.id):
            posts.append(post)
        return render_template('index.html', posts=posts)
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


@main.route('/post', methods=['GET', 'POST'])
@login_required
def posts():
    if request.method == 'POST':
        title = request.form['post_title']
        body = request.form['editormd-markdown-doc']
        date = datetime.now()
        user = current_user
        if request.form['post_title']:
            post = Post(user=user.id, title=title, body=body, date=date)
            post.save()
            posts = []
            for post in Post.objects(user=user.id):
                posts.append(post)
            return render_template('index.html', posts=posts)
    return render_template('posts.html')


@main.route('/post/<string:title>')
@login_required
def getpost(title):
    if title:
        posts = []
        for post in Post.objects(title=title):
            posts.append(post)
        if post is not None:
            return render_template('index.html', posts=posts)
    return redirect(url_for('main.main_index'))
