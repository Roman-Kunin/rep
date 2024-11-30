number = int(input("Enter a number: "))
break_number = []
if_prime = True

for i in range(2, number):
    if number % i == 0:
        if_prime = False
        break_number.append(i)

print()
if number <= 1:
    print(f"Number {number} is not prime because it's equals or less than \"1\".")
elif if_prime is True:
    print(f"Number {number} is prime.")
else:
    print(f"Number {number} is not prime because it is divided by \"{str(break_number)}\".")
