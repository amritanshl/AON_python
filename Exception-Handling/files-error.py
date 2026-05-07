# Attempting to read a configuration file
file_name = "settings.txt"

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Attempt to read the content
        content = file.read()
        print("File loaded successfully!")
except FileNotFoundError:
    # If the file doesn't exist, we provide a fallback instead of crashing
    print(f"Error: The file '{file_name}' was not found. Using default settings.")
except Exception as e:
    # A 'catch-all' for any other unexpected errors
    print(f"An unexpected error occurred: {e}")