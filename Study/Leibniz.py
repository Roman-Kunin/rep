p = 0
num_1 = 4
num_2 = 1
plus_minus = 1

for i in range(1, 1000000):
    p += (num_1 / num_2) * plus_minus
    num_2 += 2
    plus_minus *= -1

print(p)
