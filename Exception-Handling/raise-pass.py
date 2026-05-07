def set_password(new_password):
    # Checking a business rule: Password must be at least 8 characters
    if len(new_password) < 8:
        # We manually trigger a ValueError with a custom message
        raise ValueError("Security Error: Password is too short! Must be 8+ chars.")
    
    # This line only runs if the 'raise' wasn't triggered
    print("Password successfully updated.")

try:
    # Testing the rule with a short password
    set_password("1234567890")
except ValueError as e:
    # Catching our own custom error to show it to the user nicely
    print(f"Update Failed: {e}")