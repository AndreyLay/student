
import re
from bs4 import BeautifulSoup as BS

with open("Students.html", encoding="utf8") as f:
    s = f.read()

# Задача 1.Получаем количество учеников с помощью регулярных выражений:

li = re.findall("Нас уже [1-9]\s[0-9][0-9][0-9]\s[0-9][0-9][0-9]", s)
li1 = re.findall("Нас уже \d\s[0-9]{3}\s[0-9]{3}", s)
li2 = re.findall("Нас уже (\d\s[0-9]{3}\s[0-9]{3})", s)

print(li)
print (li1)
print (li2)

# Задача 2.Получаем количество учеников с помощью библиотеки BeautifulSoup:

soup = BS(s, "html.parser")
li3 = soup.find_all("span", class_="total-users")
print(li3[0].text)
