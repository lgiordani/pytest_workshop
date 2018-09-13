#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pytest_workshop
----------------------------------

Tests for `pytest_workshop` module.
"""
import pytest

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


def test_mul_by_zero_raises_exception():
    with pytest.raises(ValueError):
        Calc().mul(3, 0)


def test_avg_correct_average():
    assert Calc().avg([2, 5, 12, 98]) == 29.25


def test_avg_removes_upper_outliers():
    assert Calc().avg([2, 5, 12, 98], ut=90) == pytest.approx(6.333333)


def test_avg_removes_lower_outliers():
    assert Calc().avg([2, 5, 12, 98], lt=10) == 55


def test_avg_removes_upper_outliers_not_equal():
    assert Calc().avg([2, 5, 12, 98], ut=12) == pytest.approx(6.333333)


def test_avg_removes_lower_outliers_not_equal():
    assert Calc().avg([2, 5, 12, 98], lt=12) == 55


def test_avg_manages_empty_list():
    assert Calc().avg([]) == 0


def test_avg_manages_empty_list_after_outlier_removal():
    assert Calc().avg([12, 98], lt=15, ut=90) == 0


def test_avg_manages_outlier_removal_from_empty_list():
    assert Calc().avg([], lt=15, ut=90) == 0


def test_avg_manages_non_iterable_type():
    with pytest.raises(TypeError):
        Calc().avg(123)
