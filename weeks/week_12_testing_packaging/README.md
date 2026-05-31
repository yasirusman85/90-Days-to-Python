# 🟠 Week 12: Testing & Professional Python Practices

Welcome to Week 12! 🚀 Today's developers do not just write code that "works"; they write code that is clean, secure, easy to maintain, and covered by robust automated tests. This week, you will learn the core foundations of professional Python packaging, code formatting, static type checkers, **unittest**, **pytest**, and enterprise **logging**.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 78** | [Testing Philosophy](#day-78-testing-philosophy) | Unit, integration, and regression testing | Test plan diagramming |
| **Day 79** | [built-in `unittest`](#day-79-unittest-framework) | `TestCase`, asserts, test suites | Math module unit tests |
| **Day 80** | [Modern `pytest`](#day-80-pytest-framework) | Fixtures, parameterization, mocks | API route endpoints test suite |
| **Day 81** | [Code Quality](#day-81-code-quality-linters) | Black, Flake8, type hinting with Mypy | Code cleanup and lint correction |
| **Day 82** | [Project Packaging](#day-82-packaging-python-projects) | `pyproject.toml`, wheels, publishing | Build a custom pip package |
| **Day 83** | [Standard Logging](#day-83-application-logging) | Levels (DEBUG, INFO, ERROR), file outputs | Logger setup script |
| **Day 84** | [Milestone Project](#day-84-milestone-project-100-test-coverage) | Format, lint, and test a project | **Refactor and Test a Previous Project** |

---

## 📖 Daily Lessons

### Day 79: Testing with unittest
Create automated assertions to confirm your code functions as expected:
```python
import unittest

def add(x, y):
    return x + y

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
```

### Day 80: Testing with pytest
Pytest is the popular community choice for writing tests. It reduces boilerplate code and supports complex test fixtures:
```python
import pytest

@pytest.fixture
def sample_data():
    return {"id": 1, "status": "active"}

def test_status(sample_data):
    assert sample_data["status"] == "active"
```

### Day 81: Type Hinting & Linters
Format code automatically and verify static typing patterns:
```python
# Type hinted function
def greet_user(username: str) -> str:
    return f"Hello, {username}!"
```

---

### Day 84: Milestone Project: Refactoring to 100% Test Coverage
Choose one of your previous projects (e.g., the Tip Calculator, Expense Tracker, or SQL Grade database). Run code formatting and static type inspections to clean up any warnings, then write comprehensive unit and integration tests using `pytest` to achieve 100% code test coverage.
