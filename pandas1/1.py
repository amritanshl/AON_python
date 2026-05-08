import pandas as pd

# Creating data as a dictionary
data = {
    "Employee": ["Amrit", "Sunil", "Ananya"],
    "Department": ["DevOps", "Big Data", "Automation"],
    "Years_Exp": [8, 5, 3]
}

# Converting dictionary into a DataFrame
df = pd.DataFrame(data)

print("Full DataFrame:")
print(df)

# Accessing a specific column
print("\nAccessing Departments:")
print(df["Department"])

# Basic Analysis
print(f"\nAverage Experience: {df['Years_Exp'].mean()} years")