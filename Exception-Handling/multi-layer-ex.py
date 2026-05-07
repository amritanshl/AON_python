def process_data():
    try:
        # Ask user for a number
        raw_input = input("Enter a number to divide 100 by: ")
        
        # Convert string input to an integer (Potential ValueError here)
        number = int(raw_input)
        
        # Perform division (Potential ZeroDivisionError here)
        result = 100 / number
        
        print(f"100 divided by {number} is {result}")

    except Exception as e:
        print(f"Error occurred {e}")
    except ValueError:
        # Runs if the user typed "Apple" instead of "10"
        print("Invalid input! Please enter a whole number (digits only).")
    
    except ZeroDivisionError:
        # Runs if the user typed "0"
        print("Logic Error! You cannot divide by zero.")
    
    except KeyboardInterrupt:
        # Runs if the user hits Ctrl+C to stop the program
        print("\nProgram stopped by user.")
    
    except Exception as e:
        print(f"Error occurred {e}")

# Run the function
process_data()