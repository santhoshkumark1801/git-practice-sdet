"""
search_tests.py - Sample search test file for branching exercises.
"""

import pytest


class TestSearch:

    SEARCH_TERM = "laptop"   # <-- Change this in Exercise 1.3!

    def test_search_returns_results(self):
        """Search should return at least one result."""
        response = {"status": 200, "results": [{"id": 1, "name": self.SEARCH_TERM}]}
        assert response["status"] == 200
        assert len(response["results"]) > 0

    def test_search_result_matches_term(self):
        """Results should be relevant to the search term."""
        response = {"status": 200, "results": [{"id": 1, "name": self.SEARCH_TERM}]}
        assert self.SEARCH_TERM.lower() in response["results"][0]["name"].lower()

    def test_empty_search_returns_400(self):
        """Empty search term should return 400."""
        search_term = ""
        response = {"status": 400, "error": "Search term required"}
        assert response["status"] == 400
