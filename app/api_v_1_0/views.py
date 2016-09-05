#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-05 15:28:20
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask.ext.login import current_user, login_required
from flask import jsonify

from . import api
from . import githubData


@api.route('/user')
@login_required
def getUserinfo():
    if current_user.username is not None:
        username = current_user.username
        baseicdata = githubData.getBasicInfo(username)
        return jsonify(baseicdata)
