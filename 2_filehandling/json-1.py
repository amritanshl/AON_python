# import json

# # Technical Step 1: Create a Python Dictionary (the data source)
# customer_data = {
#     "account_id": 98765,
#     "name": "HDFC User",
#     "active": True,
#     "balance": 5000.75
# }

# # Technical Step 2: Open a file and use json.dump()
# with open("data.json", "w") as f:
#     # 'indent=4' makes the file human-readable (Pretty Printing)
#     json.dump(customer_data, f, indent=4)

# print("JSON file created successfully.")

import json

with open("data.json", "r") as f:
    # Technical Action: Convert file content into a Dictionary object
    data = json.load(f)

# Accessing specific data points
print(f"Customer Name: {data['name']}")
print(f"Current Balance: {data['balance']}")