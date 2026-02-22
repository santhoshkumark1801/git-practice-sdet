"""
login_tests.py - Sample test file for branching exercises.
Practice branching by editing this file on different branches.
"""

import pytest

BASE_URL = "https://example.com"


class TestLogin:

    def test_valid_login(self):
        """Test that a valid user can log in successfully."""
        username = "test_user@example.com"
        password = "SecurePass123"
        # Simulate login
        response = {"status": 200, "token": "abc123"}
        assert response["status"] == 200
        assert "token" in response

    def test_invalid_password(self):
        """Test that wrong password returns 401."""
        username = "test_user@example.com"
        password = "WrongPassword"
        response = {"status": 401, "error": "Invalid credentials"}
        assert response["status"] == 401

    def test_empty_username(self):
        """Test that empty username returns 400."""
        username = ""
        password = "SecurePass123"
        response = {"status": 400, "error": "Username required"}
        assert response["status"] == 400

    def test_locked_account(self):
        """Test that a locked account returns 403."""
        username = "locked_user@example.com"
        password = "SecurePass123"
        response = {"status": 403, "error": "Account locked"}
        assert response["status"] == 403
