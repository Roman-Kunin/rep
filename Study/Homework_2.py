import random


rand = random.randint(100, 999)

print("Случайное число:", rand)
print("Сумма цифр числа:", rand // 100 + rand // 10 % 10 + rand % 10)
