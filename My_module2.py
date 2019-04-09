from random import choice

spisok = [1, 2, 3, 4]
#spisok = []

def Rand_elem(spisok):
    if len(spisok) != 0:
        print(choice(spisok))
    else:
        print('None')

Rand_elem(spisok)