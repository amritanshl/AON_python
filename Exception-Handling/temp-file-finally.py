def process_sensitive_file():
    # Pre-defining the variable as None so finally can check it
    file_handle = None 
    
    try:
        # Attempting to open a log file
        file_handle = open("temp_report.txt", "w")
        file_handle.write("Top Secret Data")
        
        # Simulating a crash before we could manually close it
        print("Crunching numbers...")
        crash_trigger = 1 / 0 
        
    except ZeroDivisionError:
        print("Error: Math overflow occurred.")
    finally:
        # Check if the file was actually opened before trying to close it
        if file_handle:
            file_handle.close()
            print("Cleanup: 'temp_report.txt' has been closed and locked.")

process_sensitive_file()