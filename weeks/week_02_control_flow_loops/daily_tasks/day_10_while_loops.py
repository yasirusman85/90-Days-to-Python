"""
Day 10: Iteration with while Loops 🔄
------------------------------------
Practice using while loops to manage program state and construct a basic login gate.

Your Task:
Build a password-protected gateway. The program should continuously prompt the user 
to input a password. 
- If they type "python123", access is granted, and the loop terminates.
- If they type anything else, access is denied, and they are prompted again.
- Keep track of their failed attempts. If they fail 3 times, lock them out!
"""

print("=== Secure Login Gateway ===")

CORRECT_PASSWORD = "python123"
attempts = 0
max_attempts = 3
locked_out = False

# TODO: Write a while loop to prompt the user for password
# 1. Prompt the user for password input
# 2. Check if password is correct
# 3. If correct, print success and break the loop
# 4. If incorrect, increment attempts counter and print remaining attempts
# 5. If attempts reach max_attempts, set locked_out to True and break
