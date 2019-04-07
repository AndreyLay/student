def man():
    name = input("Введите имя: ")
    age = int(input('Введите возраст: '))
    city = input("Введите город проживания: ")
    print(name, ', ', age, ' год(а),', ' проживает в городе ', city, sep="")

man()
