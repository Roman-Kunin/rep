m = int(input())
answer_list = []
for i in range(1, m + 1):
    if m % (i ** 2) == 0:
        answer_list.append(i ** 2)
print(answer_list[-1])
