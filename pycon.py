#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: Viceren-Wang
# @Date:   2017-05-11 16:49:42
# @Last Modified by:   viceren
# @Last Modified time: 2017-05-12 13:27:08


class pycon(object):
    """docstring for pycon"""

    @property
    def partnum(self):
        return self._partnum

    @partnum.setter
    def partnum(self, partnum):
        self._partnum = partnum

    def print_info(self):
        print("Part Number is defined as %s" % self.partnum)


Ecase = pycon()
Ecase.partnum = "80-A-001"
Ecase.print_info()
