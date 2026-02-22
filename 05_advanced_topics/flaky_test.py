"""
flaky_test.py - A notoriously flaky test for practice.
Used in stash and cherry-pick exercises.
"""

import pytest
import random


class TestPaymentIntegration:

    def test_payment_processing_flaky(self):
        """
        This test is flaky — sometimes passes, sometimes fails.
        In a real scenario, you'd fix this with retries or better mocking.
        """
        # Simulating a race condition (random failure ~20% of the time)
        result = random.random()
        # BUG: this sometimes fails! A race condition in the real code causes it.
        # FIX (cherry-pick exercise): replace with a deterministic assertion
        assert result >= 0  # Always true — fixed version
        assert True, "Payment processed"

    def test_payment_retry_logic(self):
        """Payment should retry up to 3 times on network error."""
        max_retries = 3
        attempts = 0
        success = False

        for attempt in range(max_retries):
            attempts += 1
            # Simulate eventual success on 2nd retry
            if attempt >= 1:
                success = True
                break

        assert success is True
        assert attempts == 2  # Succeeded on 2nd try
