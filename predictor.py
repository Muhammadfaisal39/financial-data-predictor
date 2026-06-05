# Financial Data Predictor
# Step 2 — Look at the data and draw a graph

import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------
# PART 1 — Load the data
# -----------------------------------------------

# Read the CSV file into a table
df = pd.read_csv('all_stocks_5yr.csv')

print("Total rows in dataset:", len(df))
print("Companies in dataset:", df['Name'].nunique())
print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------------------
# PART 2 — Pick just one company (Apple = AAPL)
# -----------------------------------------------

# Filter only Apple rows
apple = df[df['Name'] == 'AAPL']

# Sort by date oldest to newest
apple = apple.sort_values('date')

print("\nApple stock rows:", len(apple))
print("\nApple data sample:")
print(apple.head())

# -----------------------------------------------
# PART 3 — Draw the graph
# -----------------------------------------------

# Create the graph
plt.figure(figsize=(12, 6))

# Draw a line of Apple closing prices over time
plt.plot(apple['date'], apple['close'], color='blue', linewidth=1.5)

# Add titles and labels
plt.title("Apple Stock Price (2013 - 2018)", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price in USD ($)", fontsize=12)

# Only show some dates on x-axis so it doesn't look crowded
plt.xticks(apple['date'][::100], rotation=45)

# Add a grid so it's easier to read
plt.grid(True, alpha=0.3)

# Make layout clean
plt.tight_layout()

# Save the graph as an image file
plt.savefig('apple_stock_price.png')

# Show the graph on screen
plt.show()

print("\nGraph saved as apple_stock_price.png")