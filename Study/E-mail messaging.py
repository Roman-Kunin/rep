from ast import Break
import email
import smtplib
from email.mime.text import MIMEText
import openpyxl
from openpyxl import Workbook
from datetime import *

#   Opening a workbook and sheets "Database" and "Report"
wb = openpyxl.reader.excel.load_workbook('test.xlsx')
wb.active = 0
database = wb.active

#   Parsing recipient's data from the database
recipient_list = []
i = 2
while True:
    surname = database[f'B{i}'].value
    name = database[f'C{i}'].value
    patronymic = database[f'D{i}'].value
    mail_adress = database[f'E{i}'].value
    phone_number = database[f'F{i}'].value
    if name != None:
        recipient_list.append([surname, name, patronymic, mail_adress, phone_number])
    else:
        break
    i += 1

#   Sender information
sender = 'romantop1414@gmail.com'
password = 'igmqplhndqtpmhpr'

#   Connecting to Gmail server, logging in as a sender
smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login(sender, password)

#   Sending the messages
replist = []
for data in recipient_list:
    message = f'Здравствуйте, {data[0]} {data[1]} {data[2]}.\nВаш адрес эл. почты: {data[3]}.\nВаш номер телефона: {data[4]}.\n\nВы в моей базе данных.'
    body = MIMEText(message)
    body['Subject'] = f'Здравствуйте, {data[1]} {data[2]}.'
    smtp_server.sendmail(sender, data[3], body.as_string())
    replist.append([data[3], str(datetime.now()).split()[0], str(datetime.now()).split()[1]])

#   Appending report data
wb.active = 1
report = wb.active
for rep in replist:
    report.append(rep)

#   Saving excel book
wb.save('test.xlsx')
