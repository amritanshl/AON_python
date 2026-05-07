def withdraw_funds(balance, amount):
    # Logic check: Do we have enough money?
    if amount > balance:
        # Triggering a RuntimeError because the 'system' cannot fulfill this
        raise RuntimeError(f"Insufficient Funds: You tried to take ${amount} but only have ${balance}.")
    
    # Subtract the amount if the check passed
    new_balance = balance - amount
    print(f"Withdrawal successful. New balance: ${new_balance}")

try:
    # Attempting to withdraw $1000 from a $500 account
    withdraw_funds(500, 1000)
except RuntimeError as error:
    # Display the specific error message we 'raised' above
    print(f"ATM Notice: {error}")