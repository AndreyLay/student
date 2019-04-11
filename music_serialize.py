
import json
import pickle

my_favourite_group = {'name': 'Г.М.О.','tracks': ['Последний месяц осени', 'Шапито'],
'Albums': [{'name': 'Делать панк-рок','year': 2016}, {'name': 'Шапито','year': 2014}]}

# сериализуем и выводим в консоль наш словарь с помощью модуля json

json_my_favourite_group = json.dumps(my_favourite_group)
print(json_my_favourite_group)

# сериализуем и выводим в консоль наш словарь с помощью модуля pickle

pickle_my_favourite_group = pickle.dumps(my_favourite_group)
print(pickle_my_favourite_group)

# открываем файл
with open('my_favourite_group.json', 'w', encoding='utf-8') as f:
    # преобразуем словарь в json и сохраняем в файл
    json_my_favourite_group = json.dump(my_favourite_group, f)

# открываем файл
with open('my_favourite_group.dat', 'wb') as f:
    # пишем в файл с помощью pickle
    pickle_my_favourite_group = pickle.dump(my_favourite_group, f)
