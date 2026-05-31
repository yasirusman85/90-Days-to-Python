# 🟢 Week 6: Object-Oriented Programming (OOP)

Welcome to Week 6! 🚀 This week we introduce **Object-Oriented Programming (OOP)**, one of the most powerful coding paradigms. OOP allows you to structure software by modeling real-world elements as objects that hold both data (attributes) and actions (methods). You will transition from structural scripting to creating reusable, modular blueprints.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 36** | [Classes & Objects](#day-36-classes-and-objects) | Writing class blueprints and initialising objects | Vehicle Class Blueprint |
| **Day 37** | [Instance Members](#day-37-instance-attributes-and-methods) | Methods and the crucial `self` keyword | Pet Action simulator |
| **Day 38** | [Class vs Instance](#day-38-class-vs-instance-members) | `@classmethod`, `@staticmethod` | Employee Count Tracker |
| **Day 39** | [Inheritance](#day-39-class-inheritance--method-overriding) | Subclasses and overriding code methods | Animal Kingdom hierarchy |
| **Day 40** | [Encapsulation & Properties](#day-40-encapsulation--property-decorators) | Getters, setters, and private variables | Secure User Password Class |
| **Day 41** | [Dunder Methods](#day-41-dunder-magic-methods) | Customising class behaviors (`__str__`, `__len__`) | Vector math class |
| **Day 42** | [Milestone Project](#day-42-milestone-project-virtual-bank-account-manager) | Combine OOP concepts | **Virtual Bank Account Manager** |

---

## 📖 Daily Lessons

### Day 36: Classes & Objects
A class is a blueprint, and an object is an instance created from that blueprint.
```python
class Student:
    def __init__(self, name, major):
        self.name = name  # Instance Attribute
        self.major = major
        
student_1 = Student("David", "Computer Science")
print(student_1.name) # "David"
```

### Day 39: Inheritance
Inheritance allows a child class to inherit attributes and methods from a parent class:
```python
class Animal:
    def eat(self):
        print("Eating...")

class Dog(Animal): # Dog inherits from Animal
    def bark(self):
        print("Woof!")
```

### Day 40: Encapsulation & `@property`
Prevent direct modification of class attributes by prefixing with double underscores (`__`) to make them private:
```python
class Account:
    def __init__(self, balance):
        self.__balance = balance # Private attribute

    @property
    def balance(self):
        return self.__balance
```

---

### Day 42: Milestone Project: Virtual Bank Account Management System
Build a robust command-line application using OOP. Design a parent `Account` class and children `SavingsAccount` and `CheckingAccount` subclasses. Secure the balances using encapsulation, implement deposit/withdrawal constraints, and log all transactions.
