# Step 1 — Load and Explore the Data
import pandas as pd

# Load the dataset
df = pd.read_csv('all_stocks_5yr.csv')

# See the first 5 rows
print("First 5 rows:")
print(df.head())

# See basic info
print("\nDataset shape:", df.shape)
print("\nColumn names:", df.columns.tolist())
print("\nBasic statistics:")
print(df.describe())