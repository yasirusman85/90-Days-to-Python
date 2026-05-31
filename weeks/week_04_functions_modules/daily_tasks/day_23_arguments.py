"""
Day 23: Arguments & Parameters ⚙️
----------------------------------
Explore default parameters, positional-only/keyword-only scopes, variable-length *args, 
and keyword-driven **kwargs.

Your Tasks:
1. Build an invoice generator function 'create_invoice' that accepts:
   - customer_name (positional / mandatory)
   - *items (variable items containing string product descriptions)
   - discount (keyword argument with default 0.0)
   - **metadata (custom fields like date, payment method, etc.)
2. Output a beautifully formatted invoice receipt.
"""

def create_invoice(customer_name, *items, discount=0.0, **metadata):
    # TODO: Print receipt header for customer_name
    # TODO: Loop and print all *items
    # TODO: Calculate subtotal, apply discount percentage, and print final total
    # TODO: Print any additional **metadata fields at the bottom
    pass

# Test runs
create_invoice(
    "William", 
    "Python Keyboard ($120)", "Ergonomic Mouse ($80)", 
    discount=10.0, 
    date="2026-05-31", payment="PayPal"
)
