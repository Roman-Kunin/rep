import time
import random

data_base = []
get_code = 0


def password():
    password: str = ""
    for i in range(1, 11):
        all_digits = "1234567890QWERTYUIOP{}ASDFGHJKL:|ZXCVBNM<>?qwertyuiop[]asdfghjkl;zxcvbnm,./"
        x = random.choice(all_digits)
        password += str(x)
    return password


while True:
    user_info = str(input("\nВведите фамилию, имя и отчество: "))
    if user_info == "Пользователи загружены":
        time.sleep(0.1)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.1)
        print(".")
        time.sleep(0.1)
        print("База сформирована.")
        break
    data_base.append(user_info)
    print("Вам выдан персональный код: {}.".format(get_code))
    get_code += 1

get_passwords = input("\nУкажите дальнейшие действия: ")
if get_passwords == "Получить пароли":
    while True:
        personal_code = input("\nВведите персональный код: ")
        if str(personal_code) == "Пароли получены":
            break
        user_name = data_base[int(personal_code)].split()
        print("Здравствуйте, {}. Ваш пароль: {}. Удачного дня!".format(user_name[1], password()))

print("\n\nОперация завершена. Хорошего дня.")
