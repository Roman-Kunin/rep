print("\n1. 1")
x = 1
y = 2

for i in range(1, 7):
    x = str(y) + str(x) * 2
    print("{}. {}".format(y, x))
    y += 1

print("\nДлина последней строки: {} знаков".format(len(x)), end=".")
