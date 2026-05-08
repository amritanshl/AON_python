import pandas as pd

df = pd.read_excel('data.xlsx', engine='openpyxl')
# --- CLEANING WRONG FORMAT (Dates) ---
# Convert 'Date' column to proper datetime objects
# Row 26 will be standardized, and Row 22 (NaN) will become NaT
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# --- CLEANING EMPTY CELLS (Missing Values) ---
# A. Remove rows where Date is missing (Row 22)
df.dropna(subset=['Date'], inplace=True)

# B. Fill missing Calories (Rows 18, 28) with the median
calories_median = df['Calories'].median()
df['Calories'] = df['Calories'].fillna(calories_median)

# --- CLEANING WRONG DATA (Outliers) ---
# Row 7 has 450 minutes. We'll set a logical cap at 120 minutes.
# Any duration over 120 will be replaced with the median duration.
duration_median = df['Duration'].median()
df.loc[df['Duration'] > 120, 'Duration'] = duration_median

# --- REMOVING DUPLICATES ---
# Row 11 and 12 are identical; this removes the duplicate
df.drop_duplicates(inplace=True)

# --- FILTERING ---
# Create a filtered view of high-intensity sessions (Pulse > 105)
high_intensity = df[df['Pulse'] > 105]

# 4. Save the cleaned data to a new Excel file
df.to_excel('cleaned_workout_data.xlsx', index=False, engine='openpyxl')

print("Data Cleaning Complete. 'cleaned_workout_data.xlsx' created.")
print(df.head(10))
