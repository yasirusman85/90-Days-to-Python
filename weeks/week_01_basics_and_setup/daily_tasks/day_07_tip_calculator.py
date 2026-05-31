"""
Day 7 Milestone Project: Tip & Split Calculator 💸
--------------------------------------------------
Combine everything you've learned in Week 1 (variables, inputs, casting, 
math operators, and string formatting) to build a split calculator.

Task Requirements:
1. Greet the user with a welcoming message.
2. Prompt for the total bill amount (convert to float).
3. Prompt for the tip percentage they want to give (e.g., 10, 12, 15).
4. Prompt for the number of people to split the bill (convert to int).
5. Calculate the total tip amount.
6. Calculate the total bill (bill + tip).
7. Calculate the final share per person.
8. Format all decimal outputs to exactly 2 decimal places (using f-strings).

Run and test the script from the terminal!
"""

def main():
    print("=== Welcome to the Tip & Split Calculator ===")
    
    # TODO 1: Ask for total bill amount
    bill = 0.0
    
    # TODO 2: Ask for tip percentage
    tip_percentage = 0
    
    # TODO 3: Ask for number of people splitting the bill
    people = 1
    
    # TODO 4: Calculate final values
    # Total tip = bill * (tip_percentage / 100)
    # Total bill = bill + total_tip
    # Share per person = total_bill / people
    
    # TODO 5: Print results formatted to 2 decimal places
    # Use f-strings like: f"${value:.2f}"
    print("\n--- Summary ---")
    # Output total bill, total tip, and what each person should pay below:

if __name__ == "__main__":
    main()
