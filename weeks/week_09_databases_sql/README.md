# 🟠 Week 9: Databases & SQL Basics

Welcome to Week 9! 🚀 Files are great for saving simple parameters, but they are inefficient for enterprise applications holding millions of dynamic cross-referenced records. This week, we will master persistent database integration. You will learn relational database schemas, structural query language (**SQL**), Python **SQLite** integrations, Object-Relational Mappers (**SQLAlchemy**), and enterprise **PostgreSQL** basics.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 57** | [SQL Fundamentals](#day-57-sql-basics) | Schema design, SELECT, INSERT, JOIN | SQL Syntax Exercises |
| **Day 58** | [Python SQLite](#day-58-python-sqlite-integration) | `sqlite3` module, connecting, cursors | Database creation script |
| **Day 59** | [CRUD Actions](#day-59-crud-operations) | Create, Read, Update, Delete transactions | Contact DB Editor |
| **Day 60** | [SQLAlchemy ORM](#day-60-sqlalchemy-orm) | Mapping classes to tables programmatically | OOP Database representation |
| **Day 61** | [DB Relationships](#day-61-database-relationships) | Foreign Keys, one-to-many structures | Order Tracker DB Schema |
| **Day 62** | [PostgreSQL Intro](#day-62-postgresql-databases) | Enterprise DB servers, `psycopg2` | PostgreSQL setup guide |
| **Day 63** | [Milestone Project](#day-63-milestone-project-school-grade-database-manager) | Relational DB execution | **School Grade Database Manager** |

---

## 📖 Daily Lessons

### Day 57: Relational Databases and SQL
Relational databases store tables linked by keys. Structured Query Language (SQL) is the tool used to query this data:
```sql
SELECT name, age FROM students WHERE grade = 'A';
```

### Day 58: SQLite in Python
SQLite is a lightweight, serverless relational database built directly into Python.
```python
import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name TEXT)")
connection.commit()
connection.close()
```

### Day 60: Object-Relational Mapping (SQLAlchemy)
Instead of writing raw SQL strings, ORMs allow you to interact with database records using standard Python classes and objects!

---

### Day 63: Milestone Project: School Grade Database Manager
Create a modular command-line tool connected to a SQLite database. Design two tables: `Students` and `Grades` (linked by a foreign key). The script should let users create new student records, assign numeric grades, calculate class averages using aggregate queries, and delete entries safely.
