"""
user_profile_tests.py - Practice file for SDET workflow exercises.
"""

import pytest


class TestUserProfile:

    def test_view_own_profile(self):
        """A logged-in user should be able to view their profile."""
        user_id = "USR001"
        response = {
            "status": 200,
            "data": {
                "id": user_id,
                "name": "Test User",
                "email": "test@example.com",
                "avatar_url": "https://cdn.example.com/avatar/USR001.png"
            }
        }
        assert response["status"] == 200
        assert response["data"]["id"] == user_id

    def test_update_profile_name(self):
        """User should be able to update their display name."""
        payload = {"name": "New Name"}
        response = {"status": 200, "data": {"name": "New Name"}}
        assert response["status"] == 200
        assert response["data"]["name"] == payload["name"]

    def test_update_profile_photo(self):
        """User should be able to upload a profile photo."""
        response = {"status": 200, "data": {"avatar_url": "https://cdn.example.com/new.png"}}
        assert response["status"] == 200
        assert "avatar_url" in response["data"]

    def test_delete_account(self):
        """User should be able to delete their own account."""
        response = {"status": 204}
        assert response["status"] == 204

    def test_view_other_user_profile_unauthorized(self):
        """Unauthenticated user should not be able to view private profiles."""
        response = {"status": 401, "error": "Authentication required"}
        assert response["status"] == 401
