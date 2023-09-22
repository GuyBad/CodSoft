print("Simple Calculator")
print("Here you can perform basics arthmetic calculations")
def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2
    else:
        return "Invalid operation"

# Input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Display the result
    print(f"Result: {result}")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print(f"An error occurred: {e}")
