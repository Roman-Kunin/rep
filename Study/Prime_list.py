# number = 2
# if_prime = True
# primes_amount = 0

# while primes_amount != 500:
#     if_prime = True
#     for n in range(2, number):
#         if number % n == 0:
#             if_prime = False
#             break

#     if if_prime is True:
#         primes_amount += 1
#         print(f"{primes_amount}.   {number}")
#     number += 1


prime_list = []
i = 2
while len(prime_list) != 500:
    for j in range(2, int(i**0.5)+1):
        if not (i % j):
            break
    else:
        prime_list.append(i)
    i+=1
[print(f'{ind}. {i}') for ind, i in enumerate(prime_list, start=1)]
