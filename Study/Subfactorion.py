def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
def subfactorial(n):
    multiplier = 0
    sign = 1
    for i in range(2, n + 1):
        multiplier += (1 / factorial(i)) * sign
        sign *= -1
    subfactorial = int(factorial(n) * multiplier)
    return subfactorial
def subsum(num):
    result = 0
    numlist = []
    str_num = str(num)
    for i in range(0, len(str_num)):
        numlist.append(int(str_num[i]))
    for i in numlist:
        result += subfactorial(i)
    return result
subfactorion = 0
while True:
    subfactorion += 1
    if subfactorion == subsum(subfactorion):
        print(subfactorion)
