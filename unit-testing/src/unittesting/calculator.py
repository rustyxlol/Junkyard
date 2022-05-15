"""
Basic calculator
"""


def add(x, y):
    """
    Add two numbers"""
    return x+y


def sub(x, y):
    """
    Subtract two numbers
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers
    """
    return x * y


def divide(x, y):
    """
    Divide two numbers
    """
    if y == 0:
        raise ValueError("Cannot divide by 0")
    return x / y
