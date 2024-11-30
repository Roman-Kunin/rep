import keyboard
from random import choice
from time import sleep


SLURS_COUNT = 100

keyboard.wait('space')

keyboard.send('backspace')

slurs = ['ОЛЕГ', 'СУКА', 'БЛЯТЬ', 'ПИДОР', 'ЕБЛАН', 'ГАНДОН', 'ПИДОРАС', 'МУДАК', 'ШЛЮХА', 'МАТЬ В КАНАВЕ', 'УЁБИЩЕ', 'КАК ТЕБЯ ЗЕМЛЯ НОСИТ', 'ЧМО ЕБАННОЕ', 'ОБРЫГАН ЁБАНЫЙ', 'КАК ТЕБЯ МАТЬ РОДИЛА', 'КАК ТЕБЯ ЗЕМЛЯ НОСИТ', 'МУДИЛА', 'ВОЛОСАТОЕ УЁБИЩЕ', 'БЕСПОЛЕЗНОЕ СУЩЕСТВО']


for i in range(SLURS_COUNT):
    keyboard.write(choice(slurs))
    keyboard.send('enter')
    sleep(0.07)
