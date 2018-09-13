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


def test_add_three_numbers():
    assert Calc().add(4, 5, 6) == 15


def test_add_many_numbers():
    s = range(100)

    assert Calc().add(*s) == 4950


def test_sub_two_numbers():
    assert Calc().sub(10, 3) == 7


def test_mul_two_numbers():
    assert Calc().mul(6, 4) == 24


def test_mul_many_numbers():
    s = range(1, 10)

    assert Calc().mul(*s) == 362880


def test_div_two_numbers():
    assert Calc().div(22, 2) == 11


def test_div_two_numbers_float():
    assert Calc().div(13, 2) == 6.5


def test_div_by_zero_returns_inf():
    assert Calc().div(5, 0) == "inf"
