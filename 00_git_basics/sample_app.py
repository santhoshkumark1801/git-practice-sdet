"""
sample_app.py - A simple Python app to practice git basics.
Edit this file during the git diff and staging exercises.
"""


def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference of two numbers."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of two numbers. Raises ValueError if b is 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"


def is_palindrome(text: str) -> bool:
    """Check whether a string is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
