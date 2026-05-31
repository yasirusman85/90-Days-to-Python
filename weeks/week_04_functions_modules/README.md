# 🔷 Week 4: Functions & Modularity

Welcome to Week 4! 🚀 Now that you can handle large datasets, writing long linear scripts becomes difficult to manage. This week is about **functions** and **modularity**. You will learn to break your code down into reusable, self-contained functional blocks, import standard libraries, and organize your files like a professional.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 22** | [Defining Functions](#day-22-defining-functions) | Parameters, arguments, and returns | Currency Calculator Function |
| **Day 23** | [Arguments & Parameters](#day-23-arguments-and-parameters) | Default params, `*args`, and `**kwargs` | Flexible Invoice Formatter |
| **Day 24** | [Scope Resolution](#day-24-variable-scope) | Local, Global, and `global` keyword | Scope isolation tester |
| **Day 25** | [Lambdas & HOFs](#day-25-anonymous-functions-and-lambdas) | `lambda`, `map()`, and `filter()` | Inline text transformer |
| **Day 26** | [Standard Libraries](#day-26-standard-library-modules) | `math`, `random`, `datetime`, `os` | Guessing games & directory checker |
| **Day 27** | [Custom Modules](#day-27-designing-custom-modules) | Splitting files, creating custom packages | Geometry formulas module |
| **Day 28** | [Milestone Project](#day-28-milestone-project-hangman-cli) | Construct modular utilities | **Word Guessing (Hangman CLI)** |

---

## 📖 Daily Lessons

### Day 22: Defining Functions
Functions allow you to isolate code block logic and repeat it whenever needed.
```python
def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    return width * height

result = calculate_area(5, 10)
print(result) # 50
```

### Day 23: Arguments and Parameters
*   **Default Arguments**: Assign default values to arguments if omitted.
*   **`*args`**: Collect positional arguments into a tuple.
*   **`**kwargs`**: Collect keyword arguments into a dictionary.

```python
def make_sandwich(bread="Wheat", *fillings):
    print(f"Making sandwich on {bread} bread with: {fillings}")

make_sandwich("White", "Ham", "Cheese", "Lettuce")
```

### Day 24: Variable Scope
Variables created inside functions reside in the local scope, while variables defined in the main block reside in the global scope.

### Day 25: Anonymous Functions & Lambdas
Write short, one-line functions using `lambda`:
```python
multiply = lambda x, y: x * y
print(multiply(3, 4)) # 12
```

---

### Day 28: Milestone Project: Word Guessing (Hangman CLI)
Build a modular console-based Hangman game where the player has to guess a hidden word character-by-character. Separate your logic into distinct functions: `get_random_word()`, `display_board()`, `check_guess()`, and `run_game()`.
