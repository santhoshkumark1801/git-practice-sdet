"""
inventory_tests.py - Practice file for advanced git topics.
Used in git stash and git bisect exercises.
"""

import pytest


EXPECTED_STOCK = 100   # <-- git bisect: change this to a wrong value in one commit


class TestInventory:

    def test_check_stock_level(self):
        """Stock level should match expected inventory."""
        actual_stock = 100
        assert actual_stock == EXPECTED_STOCK, f"Expected {EXPECTED_STOCK}, got {actual_stock}"

    def test_add_to_stock(self):
        """Adding 50 units should increase stock correctly."""
        current_stock = 100
        added = 50
        new_stock = current_stock + added
        assert new_stock == 150

    def test_remove_from_stock(self):
        """Removing 30 units should decrease stock correctly."""
        current_stock = 100
        removed = 30
        new_stock = current_stock - removed
        assert new_stock == 70

    def test_out_of_stock(self):
        """Stock level of 0 should be flagged as out of stock."""
        stock_level = 0
        is_out_of_stock = stock_level == 0
        assert is_out_of_stock is True

    # Exercise 5.1: This is the INCOMPLETE test (stash exercise)
    # def test_stock_level_INCOMPLETE:
    #     pass  # You'll stash this before it's done!
