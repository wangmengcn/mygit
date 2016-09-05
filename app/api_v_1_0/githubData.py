#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-09-05 14:40:04
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
import requests
from json import loads

session = requests.session()


def convertData(url):
    if url:
        data = session.get(url).text
        return loads(data)


def getBasicInfo(username):
    basicUrl = 'https://api.github.com/users/'
    if username:
        basicUrl += username
        return convertData(basicUrl)


def getFllowers(basicinfo):
    if basicinfo is not None:
        follower_url = basicinfo['followers_url']
        if follower_url:
            return convertData(follower_url)
    else:
        return 'DATA NOT AVIALIABLE'


def getFollowing(basicinfo):
    following_url = basicinfo['following_url']
    if following_url:
        return convertData(following_url)
    else:
        return 'DATA NOT AVIALIABLE'


def getStared(basicinfo):
    stared = basicinfo['starred_url']
    if stared:
        return convertData(stared)
    else:
        return 'None'


def getRepos(basicinfo):
    repos = basicinfo['repos_url']
    if repos:
        return convertData(repos)
    else:
        return None
