print("Квадратный корень 2.0.")
equation = input("Введите квадратное уравнение в приведённом виде без пробелов (ax^2+bx+c): ")
a = ""
b = ""
c = ""
list_a = []
list_b = []
list_c = []
num = 0
if equation[0] == "x":
    a = 1
else:
    while equation[num] != "x":
        list_a.append(str(equation[num]))
        num += 1
    for i in range(0, len(list_a)):
        a += list_a[i]
equation = equation.replace(str(a), "", 1)
equation = equation.replace("x^2", "", 1)
a = int(a)

if equation[1] == "x":
    b = 1
    equation = equation.replace(equation[0], "", 1)
else:
    num = 0
    while equation[num] != "x":
        list_b.append(str(equation[num]))
        num += 1
    for i in range(0, len(list_b)):
        b += list_b[i]
equation = equation.replace(str(b), "", 1)
equation = equation.replace("x", "", 1)
b = int(b)

if equation[0] == "=":
    c = 0
else:
    num = 0
    while equation[num] != "=":
        list_c.append(str(equation[num]))
        num += 1
    for i in range(0, len(list_c)):
        c += list_c[i]
c = int(c)


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
    print(f"Второй корень: x₂ = (-b + √D):2a = (-({b}) + √{d}):2*{a} = ({b * -1}+{root_d}):{2 * a} = {x_2}")


elif d == 0:
    x = -b / (2 * a)
    if x % 1 == 0:
        x = int(x)
    print(f"\nДискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
    print(f"Дискриминант равен нулю ({d} = 0), соответственно уравнение имеет один действительный корень.")
    print(f"\nКорень: x = -b:2a = -({b}):2*{a} = {b * -1}:{a * 2} = {x}")


elif d < 0:
    x_1 = (-b - (d ** 0.5)) / 2 * a
    x_2 = (-b + (d ** 0.5)) / 2 * a
    print(f"\nДискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
    print(f"Дискриминант меньше нуля ({d} < 0), соответственно уравнение имеет два комплексных корня (либо не имеет"
          f" корней, если вас интересуют только действительные корни).")
    print(f"\nПервый корень: x₁ = (-b - √D):2a = (-({b})-√({d})):2*{a} = ({b * -1}-√{d * -1}i):{2 * a}")
    print(f"Второй корень: x₂ = (-b + √D):2a = (-({b})+√({d})):2*{a} = ({b * -1}+√{d * -1}i):{2 * a}")