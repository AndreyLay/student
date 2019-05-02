# Создаем класс
class Sentence:

    # В качестве свойств передаем списки возможных значений

    content = ['мама', 'мыла', 'раму']
    part_of_speech = ['существительное', 'глагол']

    # Создаем метод составляющий предложение

    def show(self):
        content1 = self.content
        print(content1[1], content1[0], content1[2])

    # Создаем метод отображающий части речи в предложении

    def show_parts(self):
        content1 = self.content
        part = self.part_of_speech
        print(content1[1], part[1])
        print(content1[0], part[0])
        print(content1[2], part[0])

# Обращаемся к классу и запускаем методы

text1 = Sentence()
text1.show()
text1.show_parts()
