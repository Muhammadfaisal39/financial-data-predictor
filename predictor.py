# Financial Data Predictor
# Step 3 — Clean the Data

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------
# PART 1 — Load the data
# -----------------------------------------------

df = pd.read_csv('all_stocks_5yr.csv')

print("=== STEP 1: RAW DATA ===")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))
print("\nColumn names:", df.columns.tolist())

# -----------------------------------------------
# PART 2 — Filter just Apple
# -----------------------------------------------

apple = df[df['Name'] == 'AAPL'].copy()
apple = apple.sort_values('date')

print("\n=== STEP 2: APPLE DATA ===")
print("Apple rows:", len(apple))

# -----------------------------------------------
# PART 3 — Check for missing values
# -----------------------------------------------

print("\n=== STEP 3: MISSING VALUES ===")
print("Missing values in each column:")
print(apple.isnull().sum())

# -----------------------------------------------
# PART 4 — Fix the date column
# -----------------------------------------------

# Right now the date column is just text like "2013-02-08"
# We need to convert it to a real date format Python understands
apple['date'] = pd.to_datetime(apple['date'])

print("\n=== STEP 4: DATE FORMAT FIXED ===")
print("Date column type:", apple['date'].dtype)
print("Earliest date:", apple['date'].min())
print("Latest date:", apple['date'].max())

# -----------------------------------------------
# PART 5 — Remove any missing rows
# -----------------------------------------------

# Count rows before cleaning
before = len(apple)

# Drop any rows that have missing values
apple = apple.dropna()

# Count rows after cleaning
after = len(apple)

print("\n=== STEP 5: CLEANING DONE ===")
print("Rows before cleaning:", before)
print("Rows after cleaning:", after)
print("Rows removed:", before - after)

# -----------------------------------------------
# PART 6 — Save clean data and draw graph
# -----------------------------------------------

# Save the clean data to a new CSV file
apple.to_csv('apple_clean.csv', index=False)
print("\nClean data saved as apple_clean.csv")

# Draw the graph with clean data
plt.figure(figsize=(12, 6))
plt.plot(apple['date'], apple['close'], color='green', linewidth=1.5)
plt.title("Apple Stock Price — Clean Data (2013 - 2018)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price in USD ($)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('apple_clean_graph.png')
plt.show()

print("\nGraph saved as apple_clean_graph.png")
print("\n✅ Data cleaning complete!")