number = 2
if_prime = True
primes_amount = 0

while primes_amount != 500:
    if_prime = True
    for n in range(2, number):
        if number % n == 0:
            if_prime = False
            break

    if if_prime is True:
        primes_amount += 1
        print(f"{primes_amount}.   {number}")
    number += 1
