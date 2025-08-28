def calculator():
    print("Simple Calculator")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    operation = input("Enter an operation (+, -, *, /,%): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '%':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 % num2
    elif operation == '/':
        if num2 == 0:
            print("Error: Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operation.")
        return

    print(f"The result is: {result}")
calculator()