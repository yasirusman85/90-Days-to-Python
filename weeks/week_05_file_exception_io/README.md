# 🟢 Week 5: Exceptions & File Operations

Welcome to Week 5! 🚀 As your programs grow more complex, you'll encounter two new major requirements: handling unpredictable user errors without crashing, and persisting data permanently so that information is saved when the program exits. This week, we will master **Exceptions** and **File Operations (TXT, CSV, and JSON)**.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 29** | [Exception Handling](#day-29-exception-handling) | `try`, `except`, `else`, `finally` | Zero-Division & Value Guard CLI |
| **Day 30** | [Custom Exceptions](#day-30-custom-exceptions) | Creating custom classes & raising exceptions | User Age Validator |
| **Day 31** | [Reading Files](#day-31-reading-files) | `open()`, reading text files safely with `with` | Log File Parser |
| **Day 32** | [Writing Files](#day-32-writing-files) | Writing and appending strings | Diary Notes Saver |
| **Day 33** | [CSV Integration](#day-33-csv-integration) | Columnar data parsing (`csv` module) | Grade sheet data importer |
| **Day 34** | [JSON Serialization](#day-34-json-serialization) | Structure hierarchies (`json` module) | User Settings Saver |
| **Day 35** | [Milestone Project](#day-35-milestone-project-personal-expense-tracker-cli) | Persistent data serialization | **Daily Personal Expense Tracker CLI** |

---

## 📖 Daily Lessons

### Day 29: Exception Handling
Catch runtime errors to prevent program crashes:
```python
try:
    number = int(input("Enter an integer: "))
    result = 10 / number
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
except ValueError:
    print("Error: That was not a valid integer!")
```

### Day 31: Reading Files Safely
Always use the `with` statement when opening files to ensure they are closed properly automatically:
```python
with open("data.txt", "r") as file:
    content = file.read()
    print(content)
```

### Day 34: JSON Serialization
JSON (JavaScript Object Notation) is the universal format for data storage and exchange:
```python
import json

user = {"name": "Emma", "skills": ["Python", "SQL"]}
# Write JSON to file
with open("user.json", "w") as file:
    json.dump(user, file, indent=4)
```

---

### Day 35: Milestone Project: Personal Expense Tracker CLI
Build a command-line expense tracker where the user can record expenses (Name, Category, Amount) and save them to a file. The application should load existing data from a `JSON` file upon startup and save new records on exit.
