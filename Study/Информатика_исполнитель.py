num_1 = 3   # Начальное число
num_2 = 172  # Конечное число

operand = 0
b = 0

operation_list = "121212"    # Список команд

while operand != num_2:
    operand = num_1
    for i in range(0, len(operation_list)):
        if operation_list[i] == "1":    # Команда "1"
            operand *= 3
        elif operation_list[i] == "2":  # Команда "2"
            operand += b
    if operand != num_2:
        b += 1

print(b)
