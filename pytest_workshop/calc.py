# -*- coding: utf-8 -*-

from functools import reduce


class Calc:
    def add(self, *s):
        return sum(s)

    def sub(self, a, b):
        return a - b

    def mul(self, *s):
        return reduce(lambda x, y: x*y, s)

    def div(self, a, b):
        return a//b
