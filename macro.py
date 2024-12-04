from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui as pg
from bs4 import BeautifulSoup
from keyboard import wait
from keyboard import press_and_release
from time import sleep
import pyperclip


service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.keybr.com/index')
time.sleep(5)

# input_element = WebDriverWait(driver, 10).until(
#     EC.visibility_of_element_located((By.XPATH, '//div[@class="uKFykFQdcQ"]/div/textarea'))
# )
src = driver.page_source
soup = BeautifulSoup(src, 'html.parser')
spans = soup.find_all('span')
megaspan = ''
text = ''
for i in spans:
    megaspan += str(i)
for i in megaspan:
    if i in 'йцукенгшщзхъфывапролджэячсмитьбю':
        text += i
print(text)
text = text.replace('', ' ')
text = ' '.join([i for ind, i in enumerate(text.split(' ')) if ind % 2 == 0])
text = text.replace('ългарскисперантоепальскийусскийкранська', '')
text = ' '.join([i for i in text.split(' ')][:-1]) + ' ' + [i for i in text.split(' ')][-1][:len([i for i in text.split(' ')][-1])//2]
print(text)
#input_element = driver.find_element(By.CLASS_NAME, 'd7mouSz05B')
# input_element.send_keys('wassup nigga')

time.sleep(5)

def paste(text: str):    
    pyperclip.copy(text)
    press_and_release('ctrl + v')


def type(text: str, interval=0.0):    
    buffer = pyperclip.paste()
    if not interval:
        paste(text)
    else:
        for char in text:
            paste(char)
            sleep(interval)
    pyperclip.copy(buffer)


type(text, 0.03)

pg.typewrite('нианианиананиоаниоаинооеаоаноеноианеоианеоаиноеиоенианоиоеониаоениоениоинеаоинеаоиаеноиоиеноиенаоиоеианоианеоианоеиоеинаоиенаоеноиеноииенониеоие')
print('всё')
print(text)
time.sleep(200)