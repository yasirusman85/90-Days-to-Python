"""
Day 22: Function Definitions 🛠️
-------------------------------
Learn how to define functions, declare parameters, write docstrings, and return values.

Your Tasks:
1. Implement a function 'convert_temp' that converts temperatures between Celsius and Fahrenheit.
2. Write a docstring describing the parameters, outputs, and formula.
3. Test your function with both conversion directions.
"""

# TODO: Define a function named convert_temp(val, scale)
# - val: numerical temperature value
# - scale: string character 'C' (Celsius) or 'F' (Fahrenheit)
# - If scale is 'C', convert to Fahrenheit using: (val * 9/5) + 32
# - If scale is 'F', convert to Celsius using: (val - 32) * 5/9
# - Return the converted value rounded to 2 decimal places.

def convert_temp(val, scale):
    """
    [Write your docstring here]
    """
    pass

# Test cases
print(f"32F to Celsius: {convert_temp(32, 'F')}°C (Expected: 0.0°C)")
print(f"100C to Fahrenheit: {convert_temp(100, 'C')}°F (Expected: 212.0°F)")
