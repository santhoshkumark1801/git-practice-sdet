"""
api_tests.py - Sample API test file for branching exercises.
"""

import pytest

API_BASE_URL = "https://api.example.com/v1"


class TestUserAPI:

    def test_get_all_users(self):
        """GET /users should return a list."""
        endpoint = f"{API_BASE_URL}/users"
        # Simulated response
        response = {"status": 200, "data": [{"id": 1, "name": "Alice"}]}
        assert response["status"] == 200
        assert isinstance(response["data"], list)

    def test_create_user(self):
        """POST /users should create and return a user."""
        payload = {"name": "Bob", "email": "bob@example.com"}
        response = {"status": 201, "data": {"id": 2, "name": "Bob"}}
        assert response["status"] == 201
        assert response["data"]["name"] == payload["name"]

    def test_get_user_by_id(self):
        """GET /users/{id} should return a single user."""
        user_id = 1
        response = {"status": 200, "data": {"id": 1, "name": "Alice"}}
        assert response["status"] == 200
        assert response["data"]["id"] == user_id

    def test_delete_user(self):
        """DELETE /users/{id} should return 204."""
        user_id = 1
        response = {"status": 204}
        assert response["status"] == 204
