# 🟠 Week 10: Web Development with FastAPI

Welcome to Week 10! 🚀 This week, we transition from console-bound applications to building modern web applications. You will learn the mechanics of the internet (HTTP requests, headers, REST architecture), set up the ultra-fast **FastAPI** web framework, parse parameters, validate inputs using **Pydantic**, build persistent endpoints, and serve interactive HTML web pages using **Jinja2** templates.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 64** | [HTTP & REST](#day-64-http-and-rest) | GET, POST, PUT, DELETE methods | API Structure Diagramming |
| **Day 65** | [FastAPI Basics](#day-65-getting-started-with-fastapi) | Installation, Uvicorn, custom routes | "Hello World" endpoint |
| **Day 66** | [Request Parameters](#day-66-request-parameters) | Path vs Query params, type casting | User info retriever API |
| **Day 67** | [Pydantic Schemas](#day-67-pydantic-validation) | Data structures, input validators | Request validation gateway |
| **Day 68** | [Persistent API](#day-68-database-connected-endpoints) | Connecting endpoints to database models | DB-backed user register |
| **Day 69** | [Jinja2 Templates](#day-69-jinja2-html-rendering) | Rendering frontend HTML pages | Multi-page dynamic site |
| **Day 70** | [Milestone Project](#day-70-milestone-project-restful-todo-api) | RESTful server engineering | **Fully Functional RESTful Todo API** |

---

## 📖 Daily Lessons

### Day 64: HTTP and REST API Architecture
Web communications are transaction-based. A client sends a request (GET, POST, etc.) and a server processes it and sends back a response, containing a status code (e.g., 200 OK, 404 Not Found) and data (usually in JSON format).

### Day 65: Getting Started with FastAPI
FastAPI is a modern, high-performance web framework for building APIs with Python:
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI Server!"}
```
Run the server using Uvicorn:
```bash
uvicorn main:app --reload
```

### Day 67: Pydantic Validation
Pydantic ensures that incoming request payloads conform to defined data models before running any execution code:
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
```

---

### Day 70: Milestone Project: RESTful Todo API
Build a fully functioning task manager API. Implement endpoints to create tasks (POST), get all tasks or specific tasks (GET), update progress statuses (PUT), and delete items (DELETE). Ensure tasks persist inside a SQLite database and test your endpoints using the interactive documentation page automatically generated at `/docs`.
