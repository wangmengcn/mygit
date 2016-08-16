#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-14 21:18:58
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$


from flask import Flask
from flask_mongoengine import MongoEngine
from app.config import config
from app.models import User, Profile
from mongoengine import base

testapp = Flask(__name__)
testapp.config.from_object(config['default'])
db = MongoEngine(app=testapp)

user = User.objects(username='abc').first()
if user:
    profile = Profile()
    profile.user = user
    profile.location = 'ShiJiaZhuang'
    profile.job = 'coder'
    profile.position = None
    profile.filed = 'asdadadasd'

    print profile.id
    profile.save()
    print profile.id
    getprofile = Profile.objects(user=user).first()
    print getprofile
    print getprofile.filed
    print getprofile.location

id = user.id
print type(id)
print str(id)
print user.get_id

newuser = User.query(id)
testid = base.fields.ObjectIdField(newuser)
print newuser
print type(testid)
print testid.to_mongo(testid)
