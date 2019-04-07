# ЗАДАЧА 3

name_person1 = input('введите имя персонажа 1: ')

person1_dict = {'name': name_person1, 'health': 90, 'damage': 50}

name_person2 = input('введите имя персонажа 2: ')

person2_dict = {'name': name_person2, 'health': 100, 'damage': 30}

# выводим словари для двух персонажей:

print(person1_dict)
print(person2_dict)

# первый персонаж атакует, второй получает урон на величину урона первого персонажа
# по ключам вычитаем значения, обновляем словарь второго перонажа, получившего урон

def attack(person1_dict, person2_dict):
    pers1 = dict(**person1_dict)
    pers2 = dict(**person2_dict)
    new_h = pers2.get('health') - pers1.get('damage')
    pers2.update({'health': new_h})
    return pers2

# отрабатывает функция attack

person2_dict = attack(person1_dict, person2_dict)

# выводим словари обоих персонажей

print(person1_dict)
print(person2_dict)


# ЗАДАЧА 4


# добавляем рекомендованный параметр - броня - первому персонажу - 1, второму - 2

person1_dict ['armor'] = 1
person2_dict ['armor'] = 2

# выводим полученные словари

print('изначальные характеристики персонажа 1: ', person1_dict)
print('изначальные характеристики персонажа 2: ', person2_dict)

# функция атаки второго персонажа первым с учетом брони с обновлением словаря второго персонажа

def attack(person1_dict, person2_dict):
    pers1 = dict(**person1_dict)
    pers2 = dict(**person2_dict)
    new_h = float(pers2.get('health')) - float(pers1.get('damage')) / float(pers2.get('armor'))
    pers2.update({'health': new_h})
    return pers2

person2_dict = attack(person1_dict, person2_dict)

# состояние словарей после последнего боя - второй персонаж потерял здоровье до 25, но остается живым)

print('после боя персонаж 1: ', person1_dict)
print('после боя персонаж 2: ', person2_dict)

