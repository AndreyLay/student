
from Lesson5.my_module1 import mk_dir, del_dir
from Lesson5.my_module2 import rand_elem

Choice = int(input('{Хотите создать директории - нажмите "1", хотите удалить - "2", хотите случайный элемент - "3": '))
if Choice == 1:
    mk_dir()
elif Choice == 2:
    del_dir()
elif Choice == 3:
    rand_elem()
else:
    print('Вы ввели неправильное значение')


