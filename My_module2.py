from random import choice

spisok = [1, 2, 3, 4]
#spisok = []

def rand_elem():
    if len(spisok) != 0:
        print(choice(spisok))
    else:
        print('None')

#rand_elem(spisok)