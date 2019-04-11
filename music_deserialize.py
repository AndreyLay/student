
import json
import pickle

# обратно из файла в объект
with open('my_favourite_group.json', 'r') as f:
    my_favourite_group = json.load(f)

print(my_favourite_group)

# обратно из файла в объект
with open('my_favourite_group.dat', 'rb') as f:
    my_favourite_group = pickle.load(f)

print(my_favourite_group)