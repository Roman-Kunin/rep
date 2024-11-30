import os
import matplotlib.pyplot as plt
import numpy as np
from math import sin


os.system('cls')
a = float(input('Введите амплитуду гармонических колебаний: '))
w = float(input('Введите циклическую частоту: '))
T = 6.28/w

print(f'\nT = 2π/ω = 6.28/{w} = {T}')

t = np.arange(0, T + 0.01, 0.01)
x = []
for i in t:
    x.append(a*sin(w*i))

x_1 = np.arange(0, T, 0.01)
y_1 = x_1 * 0

y_2 = np.arange(-a, a, 0.01)
x_2 = y_2 * 0

plt.plot(x_2, y_2, 'tab:orange', '0')
plt.plot(x_1, y_1, 'tab:orange')
plt.plot(t, x, 'g')
plt.plot(T/4, a*sin(w*T/4), 'bo', label=f't(xₘₐₓ) = {T/4}с')
plt.plot(T/4*3, a*sin(w*T/4*3), 'bo', label=f't(xₘᵢₙ) = {T/4*3}с')
plt.plot(T, 0, 'ro', label=f'Период колебаний: {T/3.14}πс')
plt.legend()
plt.show()
