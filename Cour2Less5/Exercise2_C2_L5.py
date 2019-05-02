
# СКОЛЬКО НЕ БИЛСЯ НЕ РАБОТАЕТ(((((

# Создаем класс Word

class Word:

    # В качестве свойств передаем списки возможных значений

    text = ['мама', 'мыла', 'раму']
    part_of_speech = ['существительное', 'глагол']

    # Создаем метод-конструктор для указания аргументов в скобках

    def __init__(self, text, part_of_speech):
        self.text = text
        self.part_of_speech = part_of_speech

# Обращаемся к классу с аргументами в скобках
# Получаем:
# <__main__.Word object at 0x0112FF70>
# <class '__main__.Word'>
# Но как вытащить не номера ячеек, а их значения - не знаю...

text1 = Word(0, 0)
print(text1)
print(type(text1))