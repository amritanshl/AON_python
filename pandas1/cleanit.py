import pandas as pd

# 1. Load the data
# (Assuming your data is in a CSV named 'data.csv')
df = pd.read_csv('fitness_data.csv')

# --- CLEANING EMPTY CELLS ---
# Option A: Remove rows with NULL values
# df.dropna(inplace=True) 

# Option B: Replace NULL values with a specific number (e.g., 130)
df['Calories'].fillna(130, inplace=True)

# --- CLEANING WRONG FORMAT ---
# Convert 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], format='mixed')

# Remove rows where 'Date' is still NaT (Not a Time)
df.dropna(subset=['Date'], inplace=True)

# --- CLEANING WRONG DATA ---
# Identify row 7 (Duration 450) and set it to a realistic value
df.loc[7, 'Duration'] = 45

# Or, remove rows with Duration > 120
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace=True)

# --- REMOVING DUPLICATES ---
# Identify and remove row 12 (duplicate of row 11)
df.drop_duplicates(inplace=True)

# --- FILTERING ---
# Example: Filter rows where Calories are greater than 300
high_burn = df[df['Calories'] > 300]

print("Cleaned DataFrame:")
print(df.to_string())