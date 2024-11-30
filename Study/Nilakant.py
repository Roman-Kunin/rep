p = 3
numerator = 4
denominator_1 = 2
denominator_2 = 3
denominator_3 = 4
plus_minus = 1

for i in range(1, 10000):
    p += (numerator / (denominator_1 * denominator_2 * denominator_3)) * plus_minus
    denominator_1 += 2
    denominator_2 += 2
    denominator_3 += 2
    plus_minus *= -1

print(p)
