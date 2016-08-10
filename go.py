#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:52:48
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from app import createApp

running = createApp('defualt')


if __name__ == '__main__':
    context = ('mygit.crt', 'mygit.key')
    running.run(ssl_context=context, threaded=True)
