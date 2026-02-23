"""
buggy_tests.py - A test file with intentional issues to practice revert/reset.
"""
## command to run tests: pytest buggy_tests.py
##mixed
##wrong commit
import pytest


class TestUserRegistration:

    def test_username_min_length(self):
        """Username must be at least 3 characters."""
        username = "ab"
        is_valid = len(username) >= 3
        assert is_valid == False   # Correct

    def test_username_max_length(self):
        """Username must be at most 20 characters."""
        username = "a" * 21
        is_valid = len(username) <= 20
        assert is_valid == False   # Correct

    def test_valid_email_format(self):
        """Valid email should pass validation."""
        email = "user@example.com"
        is_valid = "@" in email and "." in email
        assert is_valid == True    # <-- Change this to False in exercises (simulate a bug)

    def test_password_complexity(self):
        """Password must be at least 8 chars."""
        password = "Pass123!"
        is_valid = len(password) >= 8
        assert is_valid == True    # Correct
