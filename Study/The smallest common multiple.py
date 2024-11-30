input_1 = int(input("Введите первое число: "))
input_2 = int(input("Введите второе число: "))
num_1 = input_1
num_2 = input_2
scm = 1
multiplier_1 = 0
multiplier_2 = 0

divisor = 2
numlist_1 = []
numlist_2 = []
common_list = []

while True:
    if num_1 == 1:
        break
    elif num_1 % divisor == 0:
        num_1 = int(num_1 / divisor)
        numlist_1.append(divisor)
    else:
        divisor += 1

divisor = 2
while True:
    if num_2 == 1:
        break
    elif num_2 % divisor == 0:
        num_2 = int(num_2 / divisor)
        numlist_2.append(divisor)
    else:
        divisor += 1

if len(numlist_1) >= len(numlist_2):
    for i in numlist_1:
        common_list.append(i)

    for i in numlist_2:
        if i not in common_list:
            common_list.append(i)
elif len(numlist_1) < len(numlist_2):
    for i in numlist_2:
        common_list.append(i)

    for i in numlist_1:
        if i not in common_list:
            common_list.append(i)
common_list.sort()

for i in common_list:
    scm *= i

multiplier_1 = int(scm / input_1)
multiplier_2 = int(scm / input_2)


print(f"\n1) Раскладываем первое число на простые множители: {input_1}: {numlist_1}.")
print(f"2) Раскладываем второе число на простые множители: {input_2}: {numlist_2}.")
print(f"3) Объединяем все неповторяющиеся числа в один список: {common_list}.")
print(f"4) Перемножаем все элементы списка и получаем НОК: {scm}.")
print(f"\nЕсли {scm} — общий знаменатель дроби, то:")
print(f"1) Первую дробь умножаем на {multiplier_1}.")
print(f"2) Вторую дробь умножаем на {multiplier_2}.")
