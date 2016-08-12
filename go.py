#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-08-10 08:52:48
# @Author  : Wangmengcn (eclipse_sv@163.com)
# @Link    : https://eclipsesv.com
# @Version : $Id$
from app import createApp

running = createApp('default')


# 将flask的访问方式改为https,需要用openssl生成mygit.crt, mygit.key
if __name__ == '__main__':
    context = ('mygit.crt', 'mygit.key')
    running.run(ssl_context=context, threaded=True)
