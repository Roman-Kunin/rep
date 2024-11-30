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


print(pythagorean_theorem(4, 4))