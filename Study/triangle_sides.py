def geometric_mean(numlist):
    if len(numlist) == 0:
        return "\"geometric_mean\" error: List is empty!"
    not_int_or_float = 0
    type_list = []
    for i in numlist:
        type_list.append(i)
        if type(i) != int and type(i) != float:
            not_int_or_float = 1
    if not_int_or_float == 1:
        return f"\"geometric_mean\" error: At least one list item is not \"str\" or \"float\".\n\nClasses: {type_list}"
    else:
        product = 1
        iteration_count = 0
        for i in numlist:
            product *= i
            iteration_count += 1

        answer = round(product ** (1 / iteration_count), 2)
        return answer


def pythagorean_theorem(a, b):
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        return "\n\"pythagorean_theorem\" error: At least one item is not \"int\" or \"float\"."
    else:
        c = (a ** 2 + b ** 2) ** 0.5

        if c % 1 == 0:
            c = int(c)
        else:
            c = round(c, 2)

        return c


print("\nThis program gets two hypotenuse projections and returns three sides of a triangle.")
projection_1 = float(input("\nFirst hypotenuse projection: "))
projection_2 = float(input("Second hypotenuse projection: "))

h = geometric_mean([projection_1, projection_2])

a = pythagorean_theorem(projection_1, h)
b = pythagorean_theorem(projection_2, h)
c = projection_1 + projection_2

if a % 1 == 0:
    a = int(a)
if b % 1 == 0:
    b = int(b)
if c % 1 == 0:
    c = int(c)
if h % 1 == 0:
    h = int(h)

print(f"\nCathetus 1 = {a}")
print(f"Cathetus 2 = {b}")
print(f"Hypotenuse = {c}")
print(f"\nHeight = {h}")
