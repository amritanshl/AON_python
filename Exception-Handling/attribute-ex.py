# Simulating a user profile from a database
profile = {"username": "Coder123", "active": True}

try:
    # 1. Attempt to access a missing key (KeyError)
    email = profile["email_address"]
    
    # 2. Attempt to call a method that doesn't exist on a string (AttributeError)
    # Note: This line won't even be reached if the KeyError happens first
    profile["username"].push_to_cloud()

except KeyError:
    # Handles the missing dictionary key
    print("Data Error: The 'email_address' field is missing from the profile.")

except AttributeError:
    # Handles calling a non-existent function on an object
    print("Logic Error: The username string has no 'push_to_cloud' method.")

except Exception as e:
    # The final safety net
    print(f"Something else went wrong: {type(e).__name__}")