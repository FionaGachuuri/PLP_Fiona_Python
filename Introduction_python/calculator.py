#!/usr/bin/env python3
# creating a calculator
def main():
    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        
        # Perform the calculation based on operation
        if operation == "+":
            result = num1 + num2
            operator_name = "addition"
        elif operation == "-":
            result = num1 - num2
            operator_name = "subtraction"
        elif operation == "*":
            result = num1 * num2
            operator_name = "multiplication"
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
            operator_name = "division"
        else:
            print("Error: Invalid operation. Please use +, -, *, or /.")
            return
        
        # Print the result
        print(f"{num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
