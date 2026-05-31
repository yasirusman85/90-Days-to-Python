"""
Day 19: Dictionaries 📖
-----------------------
Practice accessing, creating, modifying, and iterating over dictionaries.

Your Task:
Build a database holding stock counts for a grocery store.
"""

inventory = {
    "apples": {"price": 0.5, "stock": 100},
    "bananas": {"price": 0.3, "stock": 150},
    "oranges": {"price": 0.6, "stock": 80}
}

def update_stock(item, qty):
    # TODO: If the item exists in inventory, add qty to its 'stock' count.
    # If the item doesn't exist, print a warning.
    pass

def sell_item(item, qty):
    # TODO: Check if item is in stock. If yes and qty is available, decrement the stock, 
    # calculate total sale price, and print a receipt. If unavailable, print warning.
    pass

# Test updates
update_stock("apples", 50)
sell_item("bananas", 10)
sell_item("peaches", 5) # Should notify item not found
