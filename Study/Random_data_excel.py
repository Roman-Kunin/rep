from csv import reader
from fileinput import filename
import openpyxl as xl
from faker import Faker
from random import randint
fk = Faker()




wb = xl.reader.excel.load_workbook(filename="main.xlsx", data_only=True)
wb.active = 1
sheet = wb.active
sheet.title = 'Database'


sheet['A1'].value = "Фамилия"
sheet['B1'].value = "Имя"
sheet['C1'].value = "Номер телефона"

for i in range(2, 102):
    name, surname, *patronymic= fk.name().split()
    number = f'+7(9{randint(10, 18)}){randint(100, 599)}-{randint(10, 99)}-{randint(10, 99)}'
    sheet[f'A{i}'].value = surname
    sheet[f'B{i}'].value = name    
    sheet[f'C{i}'].value = number


wb.save('main.xlsx')
