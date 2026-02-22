"""
payment_tests.py - Practice file for merging exercises.
Intentionally designed to create merge conflicts during exercises.
"""

import pytest

# ============================================================
# Configuration — edit this line to create merge conflicts!
# ============================================================
TIMEOUT = 30           # <-- Both Exercise 3.4 teammates will edit this line!
RETRY_COUNT = 3
BASE_URL = "https://payments.example.com/api"


class TestPaymentProcessing:

    def test_valid_credit_card_payment(self):
        """A valid credit card payment should return success."""
        payload = {
            "card_number": "4111111111111111",
            "expiry": "12/27",
            "cvv": "123",
            "amount": 99.99
        }
        response = {"status": 200, "transaction_id": "TXN001", "message": "Payment successful"}
        assert response["status"] == 200
        assert "transaction_id" in response

    def test_insufficient_funds(self):
        """Payment with insufficient funds should return 402."""
        response = {"status": 402, "error": "Insufficient funds"}
        assert response["status"] == 402

    def test_invalid_card_number(self):
        """Invalid card number should return 400."""
        response = {"status": 400, "error": "Invalid card number"}
        assert response["status"] == 400

    def test_payment_timeout(self):
        """Payment should timeout after TIMEOUT seconds."""
        assert TIMEOUT > 0, "Timeout must be positive"
        # In real code: simulate request timeout
        response = {"status": 408, "error": "Request timeout"}
        assert response["status"] == 408
