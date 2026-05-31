"""
Day 84 Milestone Project: Retrofitting Test Cases & 100% Test Coverage 🧪
-------------------------------------------------------------------------
Combine clean coding principles, pytest assertions, fixtures, and execution coverage 
by writing a comprehensive test suite for a previous codebase.

Task Requirements:
1. Examine the simple 'CalculatorLibrary' class below.
2. Formulate automated unit test assertions using 'pytest'.
3. Implement tests covering normal operations, exceptions (e.g., division by zero), 
   and custom boundary values.
4. Run tests in terminal:
   pytest day_84_test_suite.py
"""

import pytest

class CalculatorLibrary:
    def add(self, x: float, y: float) -> float:
        return x + y

    def subtract(self, x: float, y: float) -> float:
        return x - y

    def divide(self, x: float, y: float) -> float:
        if y == 0:
            raise ValueError("Cannot divide by zero!")
        return x / y


# -------------------------------------------------------------
# Pytest Unit Test Suite (TODO: Implement your test cases here)
# -------------------------------------------------------------

# TODO 1: Implement a pytest fixture that initializes the CalculatorLibrary instance.
@pytest.fixture
def calc():
    return CalculatorLibrary()

# TODO 2: Write unit test functions checking add, subtract, and divide actions.
def test_addition(calc):
    assert calc.add(2.0, 3.5) == 5.5

def test_division_by_zero(calc):
    # TODO: Verify that ValueError is raised when dividing by zero.
    # Hint: Use `with pytest.raises(ValueError):`
    pass
