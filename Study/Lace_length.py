a = int(input())
b = int(input())
length = int(input())
n = int(input())

rope_len = ((((a * (n - 1)) * 2) + a) + ((b * (n - 1)) * 2) + (length * 2))

print(rope_len)
