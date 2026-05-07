# Function to calculate a percentage safely
def calculate_grade(score, total):
    try:
        # Attempt to divide score by total and multiply by 100
        percentage = (score / total) * 100
    except ZeroDivisionError:
        # This block runs ONLY if 'total' is 0, preventing a crash
        print("ERROR: Total cannot be zero. You can't divide by nothing!")
    else:
        # This runs ONLY if the 'try' block succeeded
        print(f"Your grade is: {percentage}%")
    finally:
        # This runs no matter what (often used for cleanup)
        print("Calculation attempt finished.")

# Testing the code
calculate_grade(85, 100) # Works fine
calculate_grade(85, 0)   # Triggers the exception