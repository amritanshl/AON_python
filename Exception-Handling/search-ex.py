# A list of available stock items
warehouse_stock = ["Laptop", "Monitor", "Keyboard", "Mouse"]

def ship_item(item_name):
    try:
        # The 'Risk': .index() raises a ValueError if the item isn't in the list
        item_index = warehouse_stock.index(item_name)
    except ValueError:
        # The 'Fallback': Runs if the item isn't found
        print(f"Error: {item_name} is currently out of stock.")
    else:
        # The 'Happy Path': Runs only if we found the item
        print(f"Item found at shelf #{item_index}.")
        print(f"Dispatching {item_name} to the shipping department now.")

# Test 1: Successful path
ship_item("Monitor")
# Test 2: Error path
ship_item("Webcam")