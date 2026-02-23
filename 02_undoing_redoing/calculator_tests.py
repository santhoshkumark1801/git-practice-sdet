"""
calculator_tests.py - Practice file for undoing/redoing exercises.
Make changes here to practice git restore, reset, and revert.
"""
#Command to run tests: pytest calculator_tests.py

import pytest


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class TestCalculator:

    def test_add_two_positives(self):
        assert add(2, 3) == 5       # <-- Change to 99 in Exercise 2.1!

    def test_add_negative(self):
        assert add(-1, 1) == 0

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_multiply(self):
        assert multiply(3, 4) == 12

    def test_divide(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
