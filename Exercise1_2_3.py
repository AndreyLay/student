
# Задание1.Получаем текст из файла:

with open("text", encoding="utf8") as file:
    content = file.read()
    print(content)

# Задание2.Разбиваем текст на предложения, печатаем список и проверяем его длину:

import re

pattern1 = "\.\s+"
content1 = re.split (pattern1, content)
print("Предложения в этом тексте:", content1)
print("Количество предложений в этом тексте:", len(content1))

# Задание3.Самая используемая форма слова:

pattern2 = "[а-я,А-Я]{4,15}"
content2 = re.findall(pattern2, content)
#print(content2)
#print(len(content2))

frequency = {}

print("Самые используемые слова в этом тексте:")

for word in content2:
    count = frequency.get(word,0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

for words in frequency_list:
    if frequency[words] > 2:
        print(words, frequency[words])

# print(frequency)

