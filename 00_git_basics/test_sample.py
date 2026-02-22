"""
test_sample.py - Tests for sample_app.py.
Used during git add -p (partial staging) exercise.
"""

import pytest
from sample_app import add, subtract, multiply, divide, greet, is_palindrome


class TestArithmetic:

    def test_add(self):
        assert add(2, 3) == 5

    def test_add_negatives(self):
        assert add(-1, -1) == -2

    def test_subtract(self):
        assert subtract(10, 4) == 6

    def test_multiply(self):
        assert multiply(3, 7) == 21

    def test_divide(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero(self):
        with pytest.raises(ValueError):
            divide(5, 0)


class TestHelpers:

    def test_greet(self):
        assert greet("Alice") == "Hello, Alice!"

    def test_palindrome_true(self):
        assert is_palindrome("racecar") is True

    def test_palindrome_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_palindrome_false(self):
        assert is_palindrome("hello") is False
