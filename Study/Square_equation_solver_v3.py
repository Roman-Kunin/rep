import os
os.system('cls')
print('Квадратный корень 3.0')
equation = input("Введите квадратное уравнение в приведённом виде без пробелов (ax^2+bx+c=0): ") # Уравнение

while True:
    if equation[0] != '0' and equation.find('x^2') != -1:   # Проверка а
        a_not_zero = True
    else:
        a_not_zero = False
        break
    if equation.count('x') == 2:    # Проверка b
        b_not_zero = True
        if equation[equation.rfind('x') + 1] != '=':    # Проверка c
            c_not_zero = True
        else:
            c_not_zero = False
    else:
        b_not_zero = False
        if equation[equation.find('x') + 3] != '=':
            c_not_zero = True   # Проверка c при b == 0
        else:
            c_not_zero = False
    
    if (b_not_zero == True) and (c_not_zero == True):   # Нахождение коеффициентов
        if equation[:equation.find('x')] != '':
            a_len = len(equation[:equation.find('x')])  # Коеффициент a
            a = int(equation[:equation.find('x')])  
        else:
            a = 1
            a_len = 0
        if (equation[3 + a_len:equation.rfind('x')] != '') and (equation[3 + a_len:equation.rfind('x')] not in ['+', '-']):
            b_len = len(equation[4 + a_len:equation.rfind('x')])
            b = int(equation[3 + a_len:equation.rfind('x')])
        if equation[3 + a_len:equation.rfind('x')] == '-':
            b = -1
            b_len = 0
        if equation[3 + a_len:equation.rfind('x')] == '+':
            b = 1
            b_len = 0
        c = int(equation[5 + a_len + b_len:equation.rfind('=')])
    
    # a, b и c найдены, решаем:
    if (b_not_zero == True) and (c_not_zero == True):
        print(f'\nУравнение полное, т.к. коефициенты \'b\' и \'c\' не равны нулю.')
    elif (b_not_zero == True) and (c_not_zero == False):
        print(f'\nУравнение неполное, т.к. коефициент \'c\' равен нулю.')
    elif (b_not_zero == False) and (c_not_zero == True):
        print(f'\nУравнение неполное, т.к. коефициент \'b\' равен нулю.')
    elif (b_not_zero == False) and (c_not_zero == False):
        print(f'\nУравнение неполное, т.к. коефициенты \'b\' и \'c\' равны нулю.')
    
    print(f'\na = {a}\nb = {b}\nc = {c}')
    
    d = b ** 2 - 4 * a * c
    if d > 0:
        root_d = d ** 0.5
        x_1 = (-b - (d ** 0.5)) / 2 * a
        x_2 = (-b + (d ** 0.5)) / 2 * a
        if x_1 % 1 == 0:
            x_1 = int(x_1)
            x_2 = int(x_2)
        if root_d % 1 == 0:
            root_d = int(d ** 0.5)
        print(f"\nДискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
        print(f"Дискриминант больше нуля ({d} > 0), соответственно уравнение имеет два действительных корня.")
        print(f"\nПервый корень: x₁ = (-b - √D):2a = (-({b}) - √{d}):2*{a} = ({b * -1}-{root_d}):{2 * a} = {x_1}")
        print(f"Второй корень: x₂ = (-b + √D):2a = (-({b}) + √{d}):2*{a} = ({b * -1}+{root_d}):{2 * a} = {x_2}\n")


    elif d == 0:
        x = -b / (2 * a)
        if x % 1 == 0:
            x = int(x)
        print(f"\nДискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
        print(f"Дискриминант равен нулю ({d} = 0), соответственно уравнение имеет один действительный корень.")
        print(f"\nКорень: x = -b:2a = -({b}):2*{a} = {b * -1}:{a * 2} = {x}\n")


    elif d < 0:
        x_1 = (-b - (d ** 0.5)) / 2 * a
        x_2 = (-b + (d ** 0.5)) / 2 * a
        print(f"\nДискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
        print(f"Дискриминант меньше нуля ({d} < 0), соответственно уравнение имеет два комплексных корня (либо не имеет"
            f" корней, если вас интересуют только действительные корни).")
        print(f"\nПервый корень: x₁ = (-b - √D):2a = (-({b})-√({d})):2*{a} = ({b * -1}-√{d * -1}i):{2 * a}")
        print(f"Второй корень: x₂ = (-b + √D):2a = (-({b})+√({d})):2*{a} = ({b * -1}+√{d * -1}i):{2 * a}\n")
        
    break


if a_not_zero == False:
    print('\n\'a\' не должен быть равен 0\n')

