import os
import webbrowser
import time
import random


os.system('cls')

print('Вас приветствует бот \"гейм-консультант\".')
input('\nНажмите Enter чтобы я подобрал вам игру мечты.')

os.system('cls')

inf = list(str(input('Расскажите немного о себе:\n\n')).lower().replace('.', '').replace(',', '').replace('!', '').split())

os.system('cls')

time.sleep(0.5)
print('Я знаю, что эта игра вам подойдёт!')
time.sleep(3)

kw_list_1 = ['роняли', 'детдом', 'детдоме', 'приёмный', 'детдома', 'приёмная', 'били', 'ронял', 'бил', 'била', 'роняла']
kw_list_2 = ['мать', 'канаве', 'отчим', 'отчима', 'отца', 'сдохла', 'отчимы', 'трассе', 'безмамный', 'два', 'шлюха', 'сосал']
kw_list_3 = ['16', 'шестнадцать', 'семнадцать', 'восемнадцать', '17', '18', '19']
kw_list_4 = ['5', '6', '7,', '8', 'пять', 'шесть', 'семь', 'восемь']
if_nothing = 1
for i in inf:
    if i in kw_list_1:
        webbrowser.open(random.choice(['https://www.roblox.com', 'https://kopatel-online.ru', 'https://www.epicgames.com/fortnite/ru/home']), new=2)
        if_nothing = 0
        break
    elif i in kw_list_2:
        webbrowser.open(random.choice(['https://store.steampowered.com/app/570/Dota_2/']), new=2)
        if_nothing = 0
        break
    elif i in kw_list_3:
        webbrowser.open(random.choice(['https://store.steampowered.com/app/730/CounterStrike_Global_Offensive/', 'https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/', 'https://store.steampowered.com/app/1085660/Destiny_2/', 'https://store.steampowered.com/app/739630/Phasmophobia/']), new=2)
        if_nothing = 0
        break
    elif i in kw_list_4:
        webbrowser.open(random.choice(['https://store.steampowered.com/app/444090/Paladins/', 'https://store.steampowered.com/app/440/Team_Fortress_2/', 'https://store.steampowered.com/app/1172470/Apex_Legends/', 'https://store.steampowered.com/app/252950/Rocket_League/']), new=2)
        if_nothing = 0
        break


time.sleep(1)
os.system('cls')
