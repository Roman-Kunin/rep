import random

x = int(input("\nСколько знаков нужно в паролях: "))
y = int(input("Сколько нужно паролей: "))


print("\nВаши пароли: ")


def password(z):
    y = ""
    for i in range(1, z + 1):
        all_digits = "1234567890QWERTYUIOP{}ASDFGHJKL:|ZXCVBNM<>?qwertyuiop[]asdfghjkl;zxcvbnm,./"
        z = random.choice(all_digits)
        y += str(z)
    return y


for i in range(1, y + 1):
    print("{}. ".format(i), end="")
    print(password(x))

print("\n\nОперация завершена.")
