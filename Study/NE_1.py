numlist_1 = []
numlist_1_len = int(input())
divisor = 0

for i in range(0, numlist_1_len):
    num = int(input())
    if num % 8 == 0:
        numlist_1.append(num)
        divisor += 1

if len(numlist_1) == 0:
    print("NO")
else:
    if (sum(numlist_1) / divisor) % 1 == 0:
        print(int(sum(numlist_1) / divisor))

    elif (sum(numlist_1) / divisor) % 1 != 0:
        print(sum(numlist_1) / divisor)
