"""
Day 63 Milestone Project: School Grade Database Manager 🎓
----------------------------------------------------------
Combine Relational Database structures, SQL queries, and Python CRUD transactions 
by engineering a SQLite-backed School Grade Database Manager.

Task Requirements:
1. Create a SQLite database called 'school.db' and construct two tables:
   - Students: id (INTEGER PRIMARY KEY), name (TEXT)
   - Grades: student_id (INTEGER FOREIGN KEY), subject (TEXT), score (REAL)
2. Implement functions for:
   - add_student(name)
   - add_score(student_id, subject, score)
   - view_report_card(student_id) -> Displays student name, courses, and overall average score.
3. Handle exceptions for database connectivity.
"""

import sqlite3

DB_FILE = "school.db"

def init_database():
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()
    
    # TODO: Create tables for Students and Grades with relational foreign key
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject TEXT NOT NULL,
        score REAL NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id)
    )
    """)
    
    connection.commit()
    connection.close()

def add_student(name):
    # TODO: Execute INSERT INTO students table
    pass

def add_score(student_id, subject, score):
    # TODO: Execute INSERT INTO grades table
    pass

def view_report_card(student_id):
    # TODO: Run a JOIN query to fetch student name, subjects, and scores.
    # Calculate average score and print out.
    pass

def main():
    init_database()
    print("=== School Grade Database Active ===")
    # Mock testing DB insertions
    add_student("Sophia")
    add_score(1, "Mathematics", 95.0)
    add_score(1, "Science", 88.5)
    
    view_report_card(1)

if __name__ == "__main__":
    main()
