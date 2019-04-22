
# Задание1.Получаем текст из файла:

with open("text", encoding="utf8") as file:
    content = file.read()
    print(content)

# Задание2.Разбиваем текст на предложения, печатаем список и проверяем его длину:

import re
from collections import Counter

pattern1 = "\.\s+"
content1 = re.split (pattern1, content)
print("Предложения в этом тексте:", content1)
print("Количество предложений в этом тексте:", len(content1))

# Задание3.Самая используемая форма слова:

pattern2 = "[а-я,А-Я]{4,15}"
content2 = re.findall(pattern2, content)

counter = Counter(content2)
print("Самые используемые слова в этом тексте:", counter.most_common(3))