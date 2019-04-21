import re

with open("text", encoding="utf8") as file:
    content = file.read()
    # print(content)

# Задание 4.Отбираем все ссылки(не понимаю, почему не возвращает ссылку начинающуюся на цифру):

pattern4 = "\w+.\w+.\w+/\w+"
content4 = re.findall (pattern4, content)
print("Ссылки в этом тексте:", content4)

# Задание 5.Самые частые ссылки на домен.

pattern5 = "(\w+.\w+)/"
content5 = re.findall (pattern5, content)

frequency = {}
for word in content5:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    if frequency[words] > 1:
        print("Самые частые ссылки на домен:", words, frequency[words])

# Задание 6.Закрытие ссылок.

content6 = re.sub(pattern4, "Ссылка отобразится после регистрации", content)
print(content6)