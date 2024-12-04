import keyboard
import pyautogui as pg
import time
import pyperclip

keyboard.wait('ctrl')
time.sleep(0.5)


def paste(text: str):    
    pyperclip.copy(text)
    keyboard.press_and_release('ctrl + v')


def type(text: str, interval=0.0):    
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            time.sleep(interval)
    pyperclip.copy(buffer)

type('there help', 0.1)

