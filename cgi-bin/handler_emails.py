import cgi

from htmlgrabbing import WebHTMLParser
from databaseconnector import SQLighter

'''Обработка строк'''
form = cgi.FieldStorage()
link = form.getfirst("get_link", "none")

try:
    # создание экземпляра класса-парсера
    lp = WebHTMLParser(link)

    print("Content-type: text/html\n")
    print(lp.get_mails())

    # подключение к БД и добавление результата
    db_obj = SQLighter("links.db")

    db_obj.add_row_mails(link, lp.get_mails())

    db_obj.close()

    # удаление экзмляра класса-парсера
    lp.__del__()
except:
    print("Content-type: text/html\n")
    print('Forbidden.')
