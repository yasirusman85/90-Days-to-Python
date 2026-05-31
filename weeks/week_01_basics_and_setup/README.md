# 🔷 Week 1: Python Basics & Environment Setup

Welcome to Week 1 of your Python journey! 🚀 This week is designed to lay a rock-solid foundation. You will set up a professional developer environment, understand how computers store information using variables, learn to perform calculations, manipulate text, and build your very first interactive command-line utility.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 1** | [Environment Setup](#day-1-environment-setup) | Python, VS Code, Git/GitHub | Verify installation & push first commit |
| **Day 2** | [Variables & Types](#day-2-variables-and-primitive-data-types) | `int`, `float`, `str`, `bool` | Variable assignment challenge |
| **Day 3** | [Casting & I/O](#day-3-casting-and-input--output) | `input()`, `print()`, type conversions | User Profile Generator |
| **Day 4** | [Operators](#day-4-mathematical-and-logical-operators) | Arithmetic, Comparison, Modulo | Mathematical Expression Evaluator |
| **Day 5** | [String Formatting](#day-5-string-manipulation--formatting) | f-strings, indexing, string methods | Sentence Editor & Word Swapper |
| **Day 6** | [PEP 8 & Comments](#day-6-pep-8-style-guide--clean-code) | Clean code principles, docstrings | Refactor spaghetti code to PEP 8 standard |
| **Day 7** | [Milestone Project](#day-7-milestone-project-tip--split-calculator) | Putting it all together | **Interactive Tip & Split Calculator** |

---

## 📖 Daily Lessons

### Day 1: Environment Setup
To code effectively, you need a professional environment. Today, we install and configure:
1. **Python 3**: Download and install the latest stable version from [python.org](https://www.python.org/downloads/). Ensure you check **"Add Python to PATH"** during Windows installation.
2. **VS Code**: The industry standard lightweight text editor. Install extensions: *Python* and *Pylance*.
3. **Git**: Version control software to track history and push to GitHub.
*   **Daily Task**: Create a file named `day_01_setup.py` inside `daily_tasks/` and run:
    ```python
    import sys
    print("Python Installation Success!")
    print(f"Python Version: {sys.version}")
    ```

---

### Day 2: Variables and Primitive Data Types
Variables are containers for storing data values. Python has four core primitive types:
*   `int` (Integer): Whole numbers (e.g., `42`, `-7`)
*   `float` (Floating Point): Decimal numbers (e.g., `3.1415`, `-0.01`)
*   `str` (String): Text surrounded by quotes (e.g., `"Hello"`, `'Python'`)
*   `bool` (Boolean): Logical states (`True` or `False`)

Python uses **dynamic typing**, meaning you don't need to declare types explicitly:
```python
age = 25          # int
pi = 3.14159      # float
name = "Alice"    # str
is_learning = True # bool
```

---

### Day 3: Casting and Input / Output
*   **Reading Input**: Use the `input("prompt")` function. **Important**: `input()` always returns a string!
*   **Type Casting**: To convert types, wrap variables in conversion functions:
    *   `int("10")` -> `10`
    *   `float("3.14")` -> `3.14`
    *   `str(100)` -> `"100"`
*   **Example**:
    ```python
    age_str = input("Enter your age: ")
    age_int = int(age_str)  # Converts string input to an integer for calculations
    years_left = 100 - age_int
    print("You will turn 100 in " + str(years_left) + " years!")
    ```

---

### Day 4: Mathematical and Logical Operators
Python supports standard arithmetic:
*   Addition: `+`, Subtraction: `-`, Multiplication: `*`, Division: `/` (always returns a float!)
*   Exponentiation (Power): `**` (e.g., `2 ** 3` is `8`)
*   Floor Division (ignores decimals): `//` (e.g., `7 // 2` is `3`)
*   Modulo (Remainder): `%` (e.g., `7 % 2` is `1` - useful to check odd/even numbers!)

---

### Day 5: String Manipulation & Formatting
Strings can be concatenated using `+`, repeated using `*`, and inspected with methods:
```python
sentence = "  python is amazing!  "
print(sentence.strip().capitalize()) # "Python is amazing!"
print(sentence.upper())              # "  PYTHON IS AMAZING!  "
```
**Modern Formatting (f-strings)**: Put variable values directly inside strings using curly braces `{}`:
```python
name = "Sarah"
score = 98.5
message = f"Congratulations {name}, your score is {score}%!"
print(message)
```

---

### Day 6: PEP 8 Style Guide & Clean Code
PEP 8 is Python's official style guide. Writing clean code makes it easy for others to read:
*   Use `snake_case` for variables and functions.
*   Put spaces around operators: `x = 5 + 3` (Not `x=5+3`).
*   Limit lines to a maximum of 79 characters.
*   Use standard comments starting with `# ` to explain complex blocks.

---

### Day 7: Milestone Project: Tip & Split Calculator
Build a command-line calculator that takes a restaurant bill, the percentage tip to leave, and the number of people splitting the bill, then outputs how much each person should pay.

**Expected Output Example:**
```text
=== Welcome to the Tip & Split Calculator ===
Enter the total bill amount: $124.50
Enter the percentage tip (e.g., 10, 12, 15): 15
How many people to split the bill? 4

--- Calculation Result ---
Total bill including tip: $143.18
Each person should pay: $35.80
```

---

## 🏋️ Weekly Exercises

Navigate to `daily_tasks/` to write your code. Once complete, compare your code with the designs inside `solutions/`.

1. **Exercise 1 (Variables)**: Create variables representing a country, its population, and its land area. Calculate its population density (population / area).
2. **Exercise 2 (Input/Casting)**: Create a currency converter. Prompt the user for a USD amount, multiply by a custom exchange rate, and output the result.
3. **Exercise 3 (Modulo)**: Write a short script that prompts for a whole number and outputs whether it is `Even` or `Odd`.
