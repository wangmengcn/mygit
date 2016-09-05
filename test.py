#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-14 21:18:58
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$

from app.api_v_1_0 import githubData

username = "wangmengcn"
userinfo = githubData.getBasicInfo(username)

print userinfo

followers = githubData.getFllowers(userinfo)
if followers:
    for item in followers:
        print item
