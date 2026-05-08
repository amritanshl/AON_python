import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data (simplified version of your dataset)
df = pd.read_csv('fitness_data.csv')
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(inplace=True) # Remove NaNs for clean plotting
df.loc[7, 'Duration'] = 45 # Fix outlier

# Plotting
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Calories'], marker='o', color='b', linestyle='dashdot')

plt.title('Calories Burned Over Time')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()


plt.scatter(df['Pulse'], df['Calories'], color='red')

plt.title('Relationship: Pulse vs Calories')
plt.xlabel('Average Pulse')
plt.ylabel('Calories')
plt.show()

plt.hist(df['Pulse'], bins=10, color='green', edgecolor='black')

plt.title('Distribution of Pulse Rates')
plt.xlabel('Pulse Range')
plt.ylabel('Frequency')
plt.show()

plt.bar(df.index, df['Duration'], color='purple')

plt.title('Duration of Each Workout Session')
plt.xlabel('Session Index')
plt.ylabel('Minutes')
plt.show()