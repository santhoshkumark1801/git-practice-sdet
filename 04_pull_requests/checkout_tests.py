"""
checkout_tests.py - Sample test file for PR exercises.
Practice opening, reviewing, and merging pull requests using this file.
"""

import pytest


class TestCheckoutFlow:

    # TODO (Exercise 4.4): Replace these hardcoded values with a pytest fixture
    TEST_USER = {"id": "USR001", "name": "Test User", "email": "test@example.com"}
    TEST_CART = [
        {"product_id": "PROD001", "name": "Laptop", "qty": 1, "price": 999.99},
        {"product_id": "PROD002", "name": "Mouse", "qty": 2, "price": 29.99},
    ]

    def test_checkout_happy_path(self):
        """A logged-in user with items in cart can complete checkout."""
        cart_total = sum(item["price"] * item["qty"] for item in self.TEST_CART)
        response = {
            "status": 200,
            "order_id": "ORD001",
            "total": cart_total,
            "message": "Order placed successfully"
        }
        assert response["status"] == 200
        assert "order_id" in response
        assert response["total"] == 1059.97

    def test_checkout_empty_cart(self):
        """Checkout with empty cart should return 400."""
        cart = []
        response = {"status": 400, "error": "Cart is empty"}
        assert response["status"] == 400
        assert "error" in response

    def test_apply_coupon_code(self):
        """Valid coupon code should apply discount."""
        coupon = "SAVE10"
        original_total = 1059.97
        discount_percent = 10
        expected_total = round(original_total * (1 - discount_percent / 100), 2)
        response = {
            "status": 200,
            "original_total": original_total,
            "discount": discount_percent,
            "final_total": expected_total
        }
        assert response["status"] == 200
        assert response["final_total"] == 953.97

    def test_checkout_out_of_stock(self):
        """Checkout with out-of-stock item should return 409."""
        response = {"status": 409, "error": "Item PROD001 is out of stock"}
        assert response["status"] == 409
        assert "out of stock" in response["error"]
