from cProfile import label
from math import sin, cos, radians
import numpy as np
import matplotlib.pyplot as plt

plt.title('Движение тела, брошенного под углом к горизонту')
plt.xlabel('Ось абсцисс', fontsize=18)
plt.ylabel('Ось ординат', fontsize=18)
plt.grid(True)

v = int(input('Введите скорость тела [м/с]: '))
a = int(input('Введите угол броска [°]: '))

t_top = v * sin(radians(a)) / 9.81
t = np.arange(0, t_top * 2, 0.01)

x = v * t * cos(radians(a))
y = v * t * sin(radians(a)) - ((9.81 * t ** 2) / (2))

x_top = v * cos(radians(a)) * t_top
y_top = v * sin(radians(a)) * t_top - ((9.81 * t_top ** 2) / (2))

x_l = v * t_top * 2 * cos(radians(a))
y_l = 0

plt.plot(x, y, 'g-', label='График движения тела')
plt.plot(x_top, y_top, 'ro', label='Наибольшая высота подъёма')
plt.plot(x_l, y_l, 'bo', label='Дальность полёта')
plt.annotate(f'x = {round(x_top, 2)}м;\ny = {round(y_top, 2)}м;\nt = {round(t_top, 2)}с', xy=(x_top * 1.01, y_top * 1.01))
plt.annotate(f'x = {round(x_l, 2)}м;\nt = {round(t_top * 2, 2)}с', xy=(x_l * 1.01, y_top * 0.01))
plt.ylim(0, y_top * 1.2)
plt.xlim(0, x_l * 1.2)
plt.legend()


plt.show()
