num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

if operator == "+":
    result = num_1 + num_2
    print(f"The result is {result}")
elif operator == "-":
    result = num_1 - num_2
    print(f"The result is {result}")
elif operator == "*":
    result = num_1 * num_2
    print(f"The result is {result}")
elif operator == "/":
    try:
        result = num_1 / num_2
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

        
    