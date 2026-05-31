# 🔷 Week 3: Core Data Structures

Welcome to Week 3! 🚀 Up until now, you've worked with single values stored in separate variables. However, real-world applications handle massive collections of dynamic data. This week, we will master Python's built-in collection types: **Lists**, **Tuples**, **Sets**, and **Dictionaries**. 

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 15** | [Lists Basics](#day-15-lists-basics) | Creating, Indexing, Slicing, and Methods | Shopping List Manager |
| **Day 16** | [List Comprehensions](#day-16-list-comprehensions) | Pythonic filter/transform inline arrays | Squares & Evens extractor |
| **Day 17** | [Tuples](#day-17-tuples) | Immutability, packing, & unpacking | Geo-Coordinate storage |
| **Day 18** | [Sets](#day-18-sets) | Uniqueness, Unions, and Intersections | Duplicate Filter tool |
| **Day 19** | [Dictionaries](#day-19-dictionaries) | Key-value records & lookup maps | Student Database Record CLI |
| **Day 20** | [Dict Comprehensions](#day-20-dictionary-comprehensions) | Inline dict generation | Frequency Counter |
| **Day 21** | [Milestone Project](#day-21-milestone-project-contact-book-cli) | Combine all four collections | **Interactive Contact Book CLI** |

---

## 📖 Daily Lessons

### Day 15: Lists Basics
Lists are ordered, mutable collections of items.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")         # Append item
fruits.insert(1, "blueberry") # Insert at specific index
print(fruits[0:2])            # Slicing: ['apple', 'blueberry']
```

### Day 16: List Comprehensions
Create lists easily using compact syntax:
```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]          # [1, 4, 9, 16, 25]
evens = [n for n in numbers if n % 2 == 0]   # [2, 4]
```

### Day 17: Tuples
Tuples are ordered but **immutable** (cannot be modified after creation).
```python
coordinates = (40.7128, -74.0060) # Latitude, Longitude
# coordinates[0] = 41.0 -> Errors!
lat, lon = coordinates            # Unpacking
```

### Day 18: Sets
Sets are unordered collections of unique elements (no duplicates).
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))        # {1, 2, 3, 4, 5, 6}
print(a.intersection(b)) # {3, 4}
```

### Day 19: Dictionaries
Dictionaries store elements as key-value pairs. They provide high-speed lookups!
```python
user = {"name": "Alex", "age": 28, "role": "Developer"}
print(user["name"]) # "Alex"
user["email"] = "alex@email.com" # Insert key-value
```

---

### Day 21: Milestone Project: Interactive Contact Book CLI
Create a console application that stores user details (Name, Phone, Email) in a list of dictionaries. The program should run in a loop and offer 4 options: Add Contact, Search Contact, View All Contacts, or Exit.
