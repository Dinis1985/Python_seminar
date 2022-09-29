# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

# Вариант 1:
from random import sample


def find_num(num, q):
    q = q if q > 0 else -q
    arr = sample(range(1, q * 2), q)
    print(arr)
    if num in arr:
        return True
    return False


print(find_num(10, -10))


# Вариант 2:
# import random
# size=int(input('Размер списка:'))
# digit=int(input('Число для поиска:'))
# list=[0]*size
# counter=0
# for i in range(size):
#     list[i]=random.randint(0,99)
#     if (list[i]==digit):
#         print('Число ',digit,' присутствует в ',i+1,' элементе списка')
#     else:
#         counter+=1
# if(counter==size):
#     print('Число ',digit,' отсутствует в списке')
# print(list)
