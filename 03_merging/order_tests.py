"""
order_tests.py - Practice file for merging exercises.
"""

import pytest


class TestOrderManagement:

    def test_create_order(self):
        """Creating an order should return 201 with order ID."""
        payload = {
            "product_id": "PROD001",
            "quantity": 2,
            "user_id": "USR001"
        }
        response = {"status": 201, "order_id": "ORD001", "total": 199.98}
        assert response["status"] == 201
        assert "order_id" in response

    def test_get_order_by_id(self):
        """Getting an order by ID should return order details."""
        order_id = "ORD001"
        response = {
            "status": 200,
            "order": {
                "id": order_id,
                "status": "pending",
                "total": 199.98
            }
        }
        assert response["status"] == 200
        assert response["order"]["id"] == order_id

    def test_cancel_order(self):
        """Cancelling an order should return 200."""
        order_id = "ORD001"
        response = {"status": 200, "message": "Order cancelled"}
        assert response["status"] == 200
