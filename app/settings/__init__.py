#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-18 15:33:56
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from flask import Blueprint

setting = Blueprint("setting", __name__)

from . import view
