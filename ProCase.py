# -*- coding: utf-8 -*-
# @Author: Viceren-Wang
# @Date:   2017-05-11 14:22:27
# @Last Modified by:   Viceren-Wang
# @Last Modified time: 2017-05-11 14:38:17


class GetAttr(object):
    """docstring for GetAttr"""
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    def print_info(self):
        print("%s" % self.id)


E = GetAttr()
E.id = 1
E.print_info()
