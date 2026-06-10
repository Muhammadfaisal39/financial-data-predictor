# Financial Data Predictor
# Step 4 — Train the Machine Learning Model

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

# -----------------------------------------------
# PART 1 — Load the clean data
# -----------------------------------------------

df = pd.read_csv('all_stocks_5yr.csv')
apple = df[df['Name'] == 'AAPL'].copy()
apple = apple.sort_values('date')
apple['date'] = pd.to_datetime(apple['date'])

print("✅ Data loaded successfully")
print("Total Apple rows:", len(apple))

# -----------------------------------------------
# PART 2 — Prepare the data for the model
# -----------------------------------------------

# Machine Learning models don't understand dates
# So we convert dates into numbers
# Example: day 1, day 2, day 3... day 1259
apple['day_number'] = range(len(apple))

# Tell the model WHAT TO LEARN FROM (input)
# We are using day number to predict price
X = apple[['day_number']]

# Tell the model WHAT TO PREDICT (output)
y = apple['close']

print("\n✅ Data prepared")
print("Input (X) shape:", X.shape)
print("Output (y) shape:", y.shape)

# -----------------------------------------------
# PART 3 — Split data into training and testing
# -----------------------------------------------

# We split data into two parts:
# 80% for TRAINING — the model learns from this
# 20% for TESTING — we test if the model learned correctly

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n✅ Data split done")
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))

# -----------------------------------------------
# PART 4 — Train the model
# -----------------------------------------------

# Create the model
model = LinearRegression()

# Train it — this is where the machine actually learns
model.fit(X_train, y_train)

print("\n✅ Model trained successfully!")

# -----------------------------------------------
# PART 5 — Test the model
# -----------------------------------------------

# Ask the model to predict prices for the test data
predictions = model.predict(X_test)

# Check how accurate the predictions are
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n=== MODEL ACCURACY ===")
print(f"Mean Absolute Error: ${mae:.2f}")
print(f"R2 Score: {r2:.4f}")
print("\nIn simple words:")
print(f"On average the model's prediction is ${mae:.2f} away from real price")
print(f"The model explains {r2*100:.1f}% of the price pattern")

# -----------------------------------------------
# PART 6 — Draw the resultsg
# -----------------------------------------------

# Create a full prediction line across all days
all_predictions = model.predict(X)

plt.figure(figsize=(14, 7))

# Draw real prices
plt.plot(apple['date'], apple['close'],
         color='blue', linewidth=1.5, label='Real Price')

# Draw predicted prices
plt.plot(apple['date'], all_predictions,
         color='red', linewidth=2, linestyle='--', label='Predicted Price')

plt.title("Apple Stock Price — Real vs Predicted", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price in USD ($)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('apple_prediction.png')
plt.show()

# -----------------------------------------------
# PART 7 — Add Random Forest Model for Comparison
# -----------------------------------------------

from sklearn.ensemble import RandomForestRegressor

# Create Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train it
rf_model.fit(X_train, y_train)

# Make predictions
rf_predictions = rf_model.predict(X_test)

# Check accuracy
rf_mae = mean_absolute_error(y_test, rf_predictions)
rf_r2 = r2_score(y_test, rf_predictions)

print("\n=== MODEL COMPARISON ===")
print(f"Linear Regression  — MAE: ${mae:.2f}  |  R2: {r2:.4f}")
print(f"Random Forest      — MAE: ${rf_mae:.2f}  |  R2: {rf_r2:.4f}")

# Which model won?
if rf_r2 > r2:
    print("\n✅ Random Forest performed better!")
else:
    print("\n✅ Linear Regression performed better!")

# Draw comparison graph
rf_all_predictions = rf_model.predict(X)

plt.figure(figsize=(14, 7))
plt.plot(apple['date'], apple['close'],
         color='blue', linewidth=1.5, label='Real Price')
plt.plot(apple['date'], all_predictions,
         color='red', linewidth=1.5, linestyle='--', label='Linear Regression')
plt.plot(apple['date'], rf_all_predictions,
         color='green', linewidth=1.5, linestyle='--', label='Random Forest')
plt.title("Apple Stock Price — Model Comparison", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price in USD ($)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('model_comparison.png')
plt.show()

print("\n✅ Comparison graph saved as model_comparison.png")

print("\n✅ Graph saved as apple_prediction.png")
print("\n🎉 Your ML model is complete!")