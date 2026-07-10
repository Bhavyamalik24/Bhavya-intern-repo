import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns

# Load the existing dataset
df = pd.read_csv("focus_bear_users.csv")

print("=== Focus Bear Dataset ===")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print(f"\nColumn names: {list(df.columns)}")
print(f"\nFirst 5 rows:")
print(df.head())
print(f"\nBasic statistics:")
print(df.describe())

print(f"\nLibrary versions:")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Seaborn: {sns.__version__}")