"""
Day 15: List Manipulations 📝
-----------------------------
Practice creating, index-referencing, slicing, and mutating lists.

Your Task:
Build a simple Shopping List Manager. Complete the functions below to append, remove, 
and list items, keeping the list sorted alphabetically.
"""

shopping_list = []

def add_item(item):
    # TODO: Add the item to shopping_list and sort the list alphabetically.
    pass

def remove_item(item):
    # TODO: Check if the item exists in shopping_list. If yes, remove it. If not, print a warning.
    pass

def view_list():
    # TODO: Loop through shopping_list and print each item with its index number (1-based).
    pass

# Test runs
add_item("Apples")
add_item("Bananas")
add_item("Milk")
print("Initial list:")
view_list()

remove_item("Milk")
print("\nAfter removing Milk:")
view_list()
