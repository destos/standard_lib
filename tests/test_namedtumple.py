from __future__ import annotations  # https://docs.python.org/3/whatsnew/3.7.html#pep-563-postponed-evaluation-of-annotations

from itertools import repeat
from typing import NamedTuple, Callable
from operator import add, sub, truediv

import pytest


class Point(NamedTuple):
    x: int
    y: int

    def _operation(self, other: Point, op: Callable):
        def do_op(the_other):
            # Do you know what this is doing?
            return Point(*tuple(map(op, self, the_other)))
        if isinstance(other, Point):
            return do_op(other)
        elif type(other) in (int, float):
            other = tuple(repeat(other, 2))
            return do_op(other)
        else:
            raise TypeError

    def __add__(self, other: Point) -> Point:
        return self._operation(other, add)

    def __sub__(self, other: Point) -> Point:
        return self._operation(other, sub)

    def __gt__(self, other: Point) -> bool:
        return self.total > other.total

    def __ge__(self, other: Point) -> bool:
        return self.total >= other.total

    def __lt__(self, other: Point) -> bool:
        return self.total < other.total

    def __le__(self, other: Point) -> bool:
        return self.total <= other.total

    @property
    def total(self):
        return self.x + self.y

    def least(self, other: Point):
        return self._operation(other, min)

    def most(self, other: Point):
        return self._operation(other, max)


def test_values(expect):
    point = Point(8, 2)
    expect(point.x) == 8
    expect(point.y) == 2

def test_subtraction(expect):
    value = Point(5, 4) - Point(2, 3)
    expect(value) == (3, 1)

def test_subtraction_int(expect):
    value = Point(5, 9) - 2
    expect(value) == (3, 7)

def test_subtraction_wrong_type(expect):
    with pytest.raises(TypeError):
        Point(5, 9) - "wrong"
    with pytest.raises(TypeError):
        Point(5, 9) - True

def test_addition(expect):
    value = Point(5, 4) + Point(2, 3)
    expect(value) == (7, 7)

def test_addition_int(expect):
    value = Point(5, 9) + 2
    expect(value) == (7, 11)

def test_addition_wrong_type(expect):
    with pytest.raises(TypeError):
        Point(5, 9) + "wrong"

def test_eq(expect):
    expect(Point(5, 5) == Point(5, 5)) == True
    expect(Point(5, 5) == Point(10, 0)) == False

def test_least(expect):
    value = Point(5, 9)
    other = Point(4, 10)
    result = value.least(other)
    expect(result) == Point(4, 9)

def test_most(expect):
    value = Point(5, 9)
    other = Point(4, 10)
    result = value.most(other)
    expect(result) == Point(5, 10)

def test_gt(expect):
    value = Point(3, 12)
    other = Point(4, 10)
    result = value > other
    expect(result) == True

def test_lt(expect):
    value = Point(5, 8)
    other = Point(4, 10)
    result = value < other
    expect(result) == True

def test_gte(expect):
    value = Point(5, 9)
    other = Point(4, 10)
    other_more = Point(10, 9)
    result = value >= other
    result_more = other_more >= value
    expect(result) == True
    expect(result_more) == True

def test_lte(expect):
    value = Point(5, 9)
    other = Point(4, 10)
    other_less = Point(4, 9)
    result = value <= other
    result_less = other_less <= value
    expect(result) == True
    expect(result_less) == True

def test_repr(expect):
    expect(repr(Point(5, 1))) == "Point(x=5, y=1)"

def test_str(expect):
    expect(str(Point(9, 10))) == "Point(x=9, y=10)"
