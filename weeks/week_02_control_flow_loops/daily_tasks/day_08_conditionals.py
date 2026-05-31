"""
Day 8: Conditional Statements 🚦
-------------------------------
Practice conditional logic checks to grade student scores.

Your Task:
Create a Grade Checker program. Prompt the user to input a percentage score (0 to 100).
Check the following conditions and print the corresponding grade:
- 90 or above: "Grade: A"
- 80 to 89: "Grade: B"
- 70 to 79: "Grade: C"
- 60 to 69: "Grade: D"
- Below 60: "Grade: F (Fail)"

Edge Cases:
Ensure that if the score entered is greater than 100 or less than 0, the program prints "Invalid Score!".
"""

print("=== Student Grade Calculator ===")

# TODO 1: Ask the user for a score and cast it to a float
score_input = input("Enter student score (0-100): ")

# TODO 2: Write conditional branches to calculate the grade
# Don't forget to handle invalid inputs (< 0 or > 100)!
