# -*- coding: utf-8 -*-

from functools import reduce


class Calc:
    def add(self, *s):
        return sum(s)

    def sub(self, a, b):
        return a - b

    def mul(self, *s):
        if not all(s):
            raise ValueError
        return reduce(lambda x, y: x*y, s)

    def div(self, a, b):
        if not b:
            return "inf"

        return a/b

    def avg(self, it, ut=None):
        if not ut:
            ut = max(it)

        _it = [x for x in it if x <= ut]

        return sum(_it)/len(_it)
