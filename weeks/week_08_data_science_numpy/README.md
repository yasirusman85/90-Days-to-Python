# 🟢 Week 8: Introduction to Data Science

Welcome to Week 8! 🚀 This week, we enter the world of **Data Science** and **Data Analysis**. Python is the undisputed king of data science. You will learn to work in interactive notebooks, manipulate massive matrix arrays with **NumPy**, clean and analyze structured datasets with **Pandas**, and create stunning charts with **Matplotlib** and **Seaborn**.

---

## 📅 Weekly Schedule

| Day | Topic | Key Focus | Project / Challenge |
| :--- | :--- | :--- | :--- |
| **Day 50** | [Data Environments](#day-50-data-science-environments) | Anaconda, Jupyter Notebooks | Boot Jupyter and create first `.ipynb` |
| **Day 51** | [NumPy Arrays](#day-51-numpy-basics) | Array creation, dimensions, vector operations | Linear vector calculator |
| **Day 52** | [NumPy Indexing](#day-52-numpy-operations) | Slicing, boolean indexing, element math | Array filtering challenge |
| **Day 53** | [Pandas Basics](#day-53-pandas-basics) | Series & DataFrames from lists/dicts | CSV Data Frame inspector |
| **Day 54** | [Pandas Wrangling](#day-54-pandas-data-wrangling) | Handling nulls, grouping, aggregates | Customer Sales analyzer |
| **Day 55** | [Data Visualization](#day-55-data-visualization) | Line, Bar, Scatter charts with Matplotlib | Student Grade plotter |
| **Day 56** | [Milestone Project](#day-56-milestone-project-exploratory-data-analysis) | Conduct data investigation | **Exploratory Data Analysis (EDA) on CSV** |

---

## 📖 Daily Lessons

### Day 50: Anaconda & Jupyter Notebooks
Unlike basic scripts, data analysis is highly visual. Jupyter Notebooks allow you to mix markdown text explanations, running code cells, and embedded charts into a single interactive document.

### Day 51: NumPy Vectors
NumPy stands for Numerical Python. It provides high-performance multidimensional arrays that are up to 100x faster than traditional Python lists:
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr * 2) # Vectorized multiplication: [2, 4, 6, 8]
```

### Day 53: Pandas DataFrames
Pandas is built on top of NumPy and provides tabular data structures (DataFrames), similar to Excel sheets:
```python
import pandas as pd

data = {"Name": ["Leo", "Sam"], "Age": [22, 25]}
df = pd.DataFrame(data)
print(df)
```

---

### Day 56: Milestone Project: Exploratory Data Analysis (EDA)
Download a sample public dataset (such as Titanic survival statistics or house price statistics), load it into a Pandas DataFrame, clean any missing parameters, group stats by demographic columns, and plot at least three distinct charts (e.g., age distribution histograms, survival bar charts) representing your findings.
