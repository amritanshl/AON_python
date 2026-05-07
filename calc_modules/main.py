# main.py
import operations  # Importing our custom module

def run_calculator():
    print(f"--- ProCalc {operations.VERSION} ---")
    
    try:
        # 1. Get User Input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nChoose Operation:")
        print("1. Add | 2. Subtract | 3. Multiply | 4. Divide")
        choice = input("Select (1/2/3/4): ")

        # 2. Logic Layer (Calling the Module Functions)
        if choice == '1':
            result = operations.add(num1, num2)
            op_name = "Addition"
        elif choice == '2':
            result = operations.subtract(num1, num2)
            op_name = "Subtraction"
        elif choice == '3':
            result = operations.multiply(num1, num2)
            op_name = "Multiplication"
        elif choice == '4':
            result = operations.divide(num1, num2)
            op_name = "Division"
        else:
            print("Invalid selection!")
            return

        # 3. Display Result
        print(f"\n{op_name} Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    run_calculator()