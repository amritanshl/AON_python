def update_user_records():
    print("Connecting to Database...")
    db_connected = True # Simulating an open connection

    try:
        # Imagine a logic error happens here
        print("Updating records...")
        raise RuntimeError("Lost connection to server mid-update!")
    except RuntimeError as e:
        # Handle the specific error
        print(f"Update failed: {e}")
    finally:
        # This code runs even though we 'raised' an error above
        db_connected = False
        print("Database connection closed safely.")

update_user_records()