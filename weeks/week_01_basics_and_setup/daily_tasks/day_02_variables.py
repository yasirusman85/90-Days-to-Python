"""
Day 2: Variables & Primitive Data Types 📦
-------------------------------------------
Let's practice creating variables and working with different types of data.

Exercises:
1. Complete the TODO blocks below by assigning correct values and types.
2. Run the script and check that the assert checks pass.
"""

# TODO 1: Create a variable named 'student_name' and assign your name as a string.
student_name = None

# TODO 2: Create a variable named 'challenge_days' and assign the integer 90.
challenge_days = None

# TODO 3: Create a variable named 'success_rate' and assign the float 98.7.
success_rate = None

# TODO 4: Create a variable named 'is_excited' and assign the boolean value True.
is_excited = None


# -------------------------------------------------------------
# Test Checks (Do not modify the lines below)
# -------------------------------------------------------------
def verify_variables():
    try:
        assert isinstance(student_name, str), "student_name must be a string!"
        assert isinstance(challenge_days, int) and challenge_days == 90, "challenge_days must be the integer 90!"
        assert isinstance(success_rate, float) and success_rate == 98.7, "success_rate must be the float 98.7!"
        assert isinstance(is_excited, bool) and is_excited is True, "is_excited must be the boolean True!"
        
        print("🎉 Exciting work! All variables declared correctly and tests passed!")
        print(f"Student: {student_name}")
        print(f"Goal: Learn Python in {challenge_days} days!")
        print(f"Success Rate Target: {success_rate}%")
        print(f"Excited to start? {'Yes!' if is_excited else 'No'}")
    except AssertionError as e:
        print(f"❌ Verification Failed: {e}")
    except NameError as e:
        print(f"❌ Name Error: Make sure you defined all required variables. Details: {e}")

if __name__ == "__main__":
    verify_variables()
