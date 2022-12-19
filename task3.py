

# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
# максимум использование библиотеки Random для и получения случайного int

import random
size = int(input("Сколько будет элементов в списке: "))
my_list = []

for i in range(size):
    my_list.append(random.randint(0, 20))
print(my_list)
caunt = 0
while caunt != size//2:
    a = my_list[0]
    my_list.pop(0)
    my_list.insert(random.randint(0, size), a)
    caunt = caunt+1
print(my_list)
