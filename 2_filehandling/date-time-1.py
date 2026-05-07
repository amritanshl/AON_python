from datetime import datetime

now = datetime.now()

# We format it: Year-Month-Day_Hour-Minute
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

filename = f"backup_{timestamp}.txt"
with open(filename, "w") as f:
    f.write("System backup completed.")
    
print(f"File created: {filename}")
# Result: backup_2026-04-20_19-15.txt