def get_next_task(tasks):
    # Logic check: Our code should never call this function if the list is empty
    # If it is empty, the developer (you) forgot to check the length elsewhere
    assert len(tasks) > 0, "Logic Error: Task list is empty. Check the feeder function!"
    
    # Remove and return the first item
    return tasks.pop(0)

# Scenario A: Works fine
print(f"Task 1: {get_next_task(['Email', 'Code'])}")

# Scenario B: This will trigger an AssertionError
print(f"Task 2: {get_next_task([])}")