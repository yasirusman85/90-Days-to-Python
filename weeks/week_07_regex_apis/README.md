# 🟢 Week 7: Advanced Modules, Regex, & APIs

Welcome to Week 7! 🚀 This week, you will connect your local Python scripts to the external internet. You will learn to perform advanced text validation with **Regular Expressions**, manipulate **Dates & Timezones**, establish isolated developer workspaces with **Virtual Environments**, write custom **Decorators**, and consume web **REST APIs** to fetch live internet data.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 43** | [Regular Expressions](#day-43-regular-expressions-regex) | `re` module, string pattern checks | Email & Phone Validator |
| **Day 44** | [Date & Time](#day-44-date-and-time) | `datetime`, formatting and UTC offsets | Flight Time Calculator |
| **Day 45** | [HTTP Requests](#day-45-http-requests) | Client-Server models, `requests` package | Website status checker |
| **Day 46** | [REST API Payloads](#day-46-rest-api-payloads) | Query parameters, JSON responses | Random Dog Image Downloader |
| **Day 47** | [Virtual Environments](#day-47-virtual-environments-venv) | `venv`, isolation, and `pip requirements` | Custom environment setup |
| **Day 48** | [Decorators](#day-48-decorators) | Wrappers, high-level abstractions | Function execution timer |
| **Day 49** | [Milestone Project](#day-49-milestone-project-live-weather-forecast-cli-app) | External API integrations | **Live Weather Forecast CLI App** |

---

## 📖 Daily Lessons

### Day 43: Regular Expressions (Regex)
Extract and match patterns within text documents:
```python
import re

text = "My email is support@learningpython.org"
match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
if match:
    print(f"Found email: {match.group()}")
```

### Day 45: HTTP Requests & Networking
Consume raw web endpoints:
```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code) # 200 (Success)
data = response.json()
print(data["current_user_url"])
```

### Day 48: Decorators
Decorators let you modify the behavior of a function without changing its source code:
```python
def my_decorator(func):
    def wrapper():
        print("Before function execution...")
        func()
        print("After function execution...")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

---

### Day 49: Milestone Project: Live Weather Forecast CLI App
Build a command-line application that prompts the user for a city name, communicates with a public API (e.g., OpenWeatherMap), processes the payload, and displays current temperatures, humidity levels, and wind conditions inside the console.
