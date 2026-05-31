"""
Day 56 Milestone Project: Exploratory Data Analysis (EDA) 📊
------------------------------------------------------------
Consolidate NumPy arrays, Pandas DataFrames, and data calculations 
by performing an Exploratory Data Analysis (EDA) on a sample dataset.

Task Requirements:
1. Generate a mock Pandas DataFrame representing monthly retail shop sales data:
   - Columns: Month, Category (Electronics, Apparel, Groceries), Sales_Amt, Dispatched_Qty.
2. Clean data parameters:
   - Identify and fill any synthetic null entries.
3. Compute analytical values:
   - Calculate total sales per category.
   - Use NumPy vector operations to compute average transaction size (Sales_Amt / Dispatched_Qty).
4. Print out analytical summaries.
"""

import pandas as pd
import numpy as np

def run_analysis():
    print("=== Exploratory Data Analysis Sandbox ===")
    
    # 1. Create a dictionary with mock data, including some missing elements (None)
    raw_data = {
        "Month": ["Jan", "Jan", "Jan", "Feb", "Feb", "Feb", "Mar", "Mar", "Mar"],
        "Category": ["Electronics", "Apparel", "Groceries", "Electronics", "Apparel", "Groceries", "Electronics", "Apparel", "Groceries"],
        "Sales_Amt": [12000.0, 8500.0, 15000.0, 14500.0, None, 16200.0, 19000.0, 9200.0, 17500.0],
        "Dispatched_Qty": [120, 250, 1500, 140, 280, 1650, 180, 270, None]
    }
    
    # TODO 1: Load dict into a Pandas DataFrame
    df = pd.DataFrame(raw_data)
    print("\n--- Raw DataFrame ---")
    print(df)
    
    # TODO 2: Handle Null Values
    # Fill Sales_Amt null with the median of Sales_Amt
    # Fill Dispatched_Qty null with the mean of Dispatched_Qty
    
    # TODO 3: Vectorized NumPy math
    # Calculate transaction sizes (Sales_Amt / Dispatched_Qty) and append to DataFrame as 'Avg_Item_Price'
    
    # TODO 4: Pandas aggregates
    # Group by Category and compute sum total of Sales_Amt and Dispatched_Qty
    
    print("\n--- Cleaned & Processed Data ---")
    print(df)

if __name__ == "__main__":
    run_analysis()
