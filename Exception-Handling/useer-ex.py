# Function to process a user's age for a digital ID
def register_user():
    age_input = input("Enter your age: ")

    try:
        # The 'Risk': Converting text to an integer might fail
        age = int(age_input)
    except ValueError:
        # The 'Safety Net': Runs if the user typed "Twenty" instead of 20
        print("Registration failed: Please use numeric digits for your age.")
    else:
        # The 'Happy Path': Runs ONLY if the conversion above worked perfectly
        print(f"Success! You are {age} years old.")
        print("Proceeding to create your digital ID profile...")

# Run the function
register_user()