#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-06-07 11:01:48
# @Last Modified by:   viceren
# @Last Modified time: 2017-06-07 11:08:23


from werkzeug.wrappers import Request, Response


@Request.application
def application(request):
    return Response('Starting wkweb')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 8080, application)
