# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке
# возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

user_number_1 = int(input("введите длину первого списка:"))
user_number_2 = int(input("введите длину второго списка:"))

list_1 = {random.randint(1, 10) for _ in range(user_number_1)}
list_2 = {random.randint(1, 10) for _ in range(user_number_2)}
print(list_1)
print(list_2)

result_list = set()
result_list = list_1.intersection(list_2)
print(result_list)
