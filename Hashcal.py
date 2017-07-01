#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-07-01 13:21:57
# @Last Modified by:   viceren
# @Last Modified time: 2017-07-01 13:26:32
import hashlib

Str = input('Please input a string: ')
Strhash = hashlib.md5(Str.encode('utf-8'))
Printhash = print(Strhash.hexdigest())
