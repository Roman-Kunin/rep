print("Квадратный корень 2.0.")
a = int(input("Введите значение переменной \"a\" (число, стоящее перед x²): "))
b = int(input("Введите значение переменной \"b\" (число, стоящее перед x): "))
c = int(input("Введите значение переменной \"c\" (число, стоящее перед \"=\"): "))

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
    print(f"Дискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
    print(f"Дискриминант равен нулю ({d} = 0), соответственно уравнение имеет один действительный корень.")
    print(f"Корень: x = -b:2a = -({b}):2*{a} = {b * -1}:{a * 2} = {x}")


elif d < 0:
    x_1 = (-b - (d ** 0.5)) / 2 * a
    x_2 = (-b + (d ** 0.5)) / 2 * a
    print(f"Дискриминант квадратного уравнения: D = b²-4ac = {b}²-4*{a}*{c} = {b ** 2}-{4 * a * c} = {d}.")
    print(f"Дискриминант меньше нуля ({d} < 0), соответственно уравнение имеет два комплексных корня (либо не имеет"
          f" корней, если вас интересуют только действительные корни).")
    print(f"Первый корень: x₁ = (-b - √D):2a = (-({b})-√({d})):2*{a} = ({b * -1}-√{d * -1}i):{2 * a}")
    print(f"Второй корень: x₂ = (-b + √D):2a = (-({b})+√({d})):2*{a} = ({b * -1}+√{d * -1}i):{2 * a}")
