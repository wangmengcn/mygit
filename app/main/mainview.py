#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:35:21
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from flask import render_template
from . import main


@main.route('/')
def main_index():
    return render_template('index.html')
