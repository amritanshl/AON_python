import logging

# basicConfig sets the 'floor' for what gets recorded. 
# Here, we set it to WARNING, so DEBUG and INFO will be ignored.
logging.basicConfig(level=logging.WARNING)

# These will NOT show up because they are below the WARNING 'floor'
logging.debug("I am a secret debug message.")
logging.info("The system has started.")

# These WILL show up in your VS Code terminal
logging.warning("Caution: The battery is at 15%.")
logging.error("Error: Could not connect to the printer.")
logging.critical("Fatal: The engine has stopped!")


import logging

# We add 'filename' to save output to a file instead of the terminal
# We use 'filemode="w"' to overwrite the file every time (use "a" to append)
logging.basicConfig(
    filename="app_history.log", 
    level=logging.INFO, 
    filemode="w"
)

# These messages won't appear in the terminal! 
# Look for a new file named 'app_history.log' in your VS Code folder.
logging.info("User 'Admin' opened the dashboard.")
logging.info("Fetching data from the cloud...")
logging.error("Failed to sync with Cloud-Server-B.")

print("Check your folder for 'app_history.log' to see the results!")