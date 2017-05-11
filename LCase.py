# -*- coding: utf-8 -*-
# @Author: Viceren-Wang
# @Date:   2016-12-14 14:59:28
# @Last Modified by:   Viceren-Wang
# @Last Modified time: 2017-05-04 10:11:35

#!  /usr/bin/env python3
#   -*- coding: utf-8 -*-

NumList = [0, 1, 2, 3, 4]
NumList.append(5)
print(list(NumList))
NumList.insert(0, -1)
print(list(NumList))
NumList.pop(0)
print(list(NumList))
NumList[5] = 5
print(list(NumList))
