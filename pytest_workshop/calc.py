# -*- coding: utf-8 -*-


class Calc:
    def add(self, *s):
        return sum(s)

    def sub(self, a, b):
        return a - b

    def mul(self, *s):
        res = 1
        for i in s:
            res = res * i

        return res
