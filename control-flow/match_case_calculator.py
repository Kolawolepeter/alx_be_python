num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")
match operator:
    case "+":
        result = num_1 + num_2
        print(f"The result is {result}.")
    case "-":
        result = num_1 - num_2
        print(f"The result is {result}.")
    case "*":
        result = num_1 * num_2
        print(f"The result is {result}.")
    case "/":
        try:
            result = num_1 / num_2
            print(f"The result is {result}")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator")