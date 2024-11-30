def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
def facsum(num):
    result = 0
    numlist = []
    str_num = str(num)
    for i in range(0, len(str_num)):
        numlist.append(int(str_num[i]))
    for i in numlist:
        result += factorial(i)
    return result
factorion = 0
while True:
    factorion += 1
    if factorion == facsum(factorion):
        print(factorion)
