operation = input("Choose the operation (+, -, *, /): ")

match operation:
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
            print(f"The result is {result}.")
        except ZeroDivisionError:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operator.")
