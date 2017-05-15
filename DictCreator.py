#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: viceren
# @Date:   2017-05-13 11:29:17
# @Last Modified by:   viceren
# @Last Modified time: 2017-05-15 10:55:41


class DictCreater(object):
    """docstring for DictCreater"""

    @property
    def Dict(self):
        return self._Dict

    @Dict.setter
    def Dict(self, Dict):
        self._Dict = Dict

    def print_info(self):
        print("Dict is : %s" % self.Dict)

Ecase = DictCreater()
Ecase.Dict = "EQQ"
Ecase.print_info()
