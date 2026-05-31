"""
Day 35 Milestone Project: Daily Personal Expense Tracker CLI 📊
---------------------------------------------------------------
Combine Exception Handling, File I/O, and JSON serialization by engineering 
a persistent Expense Tracker command-line tool.

Task Requirements:
1. Load expenses from a JSON file called 'expenses.json' upon startup.
   - If the file doesn't exist, start with an empty list.
   - Handle FileNotFoundError and JSONDecodeError gracefully.
2. In a loop, offer choices:
   - 1. View all expenses
   - 2. Add an expense (Name, Category, Amount)
   - 3. View expenses by category
   - 4. Save and Exit
3. Safely cast the Amount input to a float, handling ValueError.
4. Serialize and save the final list back to 'expenses.json' on exit.
"""

import json
import os

EXPENSE_FILE = "expenses.json"
expenses = []

def load_expenses():
    global expenses
    # TODO: Check if file exists. Load list from JSON.
    # Handle FileNotFoundError and json.JSONDecodeError.
    pass

def save_expenses():
    # TODO: Serialize and write expenses list back to EXPENSE_FILE.
    pass

def add_expense():
    print("\n--- Add Expense ---")
    name = input("Enter Item Name: ")
    category = input("Enter Category (e.g., Food, Travel, Rent): ").capitalize()
    
    # TODO: Prompt for amount. Catch ValueError to ensure it's a valid number.
    # If valid, append dictionary {"name": name, "category": category, "amount": amount}
    pass

def view_expenses():
    print("\n--- All Expenses ---")
    # TODO: Loop and print all recorded expenses. Print sum total.
    pass

def main():
    load_expenses()
    while True:
        print("\n=== Personal Expense Tracker ===")
        print("1. View All Expenses")
        print("2. Add Expense")
        print("3. Save & Exit")
        
        choice = input("Enter choice (1-3): ")
        if choice == "1":
            view_expenses()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            save_expenses()
            print("Expenses saved. Goodbye! 👋")
            break
        else:
            print("Invalid Choice!")

if __name__ == "__main__":
    main()
