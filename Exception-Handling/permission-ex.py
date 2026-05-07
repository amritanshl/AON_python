# Dictionary representing user permissions
user_permissions = {"admin": True, "editor": False}

def access_vault(role):
    try:
        # The 'Risk': Accessing a key that might not exist in our dictionary
        has_access = user_permissions[role]
    except KeyError:
        # The 'Safety Net': Runs if the role is unrecognized
        print("Access Denied: Unknown role provided.")
    else:
        # The 'Happy Path': Runs if the role was found (even if it's False!)
        if has_access:
            print("Welcome, Admin. Accessing the top-secret vault...")
        else:
            print("Access Denied: You do not have the required permissions.")

# Test it out
access_vault("admin")  # Should hit the Happy Path
access_vault("guest")  # Should hit the Exception