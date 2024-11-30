def arithmetic(num_1, num_2, operator):
    acceptable_operators = ("+", "-", "*", "/")
    if operator not in acceptable_operators:
        print("Неизвестная операция")
    else:
        if operator == "+":
            return num_1 + num_2
        elif operator == "-":
            return num_1 - num_2
        elif operator == "*":
            return num_1 * num_2
        elif operator == "/":
            return num_1 / num_2


print(arithmetic(10, 5, "+"))
