#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""
from pytest_workshop.calc import Calc


def test_add_two_numbers():
    c = Calc()

    res = c.add(4, 5)

    assert res == 9
