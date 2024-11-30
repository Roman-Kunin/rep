import random as r
with open("main_2.txt", "w") as f_1:
    for i in range(r.randint(10, 1000)):
        f_1.write(f"{r.randint(1000, 9999)}\n")
