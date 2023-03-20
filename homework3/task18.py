# Задача 18: Требуется найти в массиве A[1 ... N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.

import random
number_of_elements = int(input("введите количество элементов в массиве: "))
random_list = [random.randint(1, 10) for _ in range(number_of_elements)]
print(random_list)

found_element = int(input("какой элемент нужно найти в массиве? "))

diff = []
for i in range(number_of_elements):
    diff.append(random_list[i] - found_element)
    if diff[i] < 0:
        diff[i] = -diff[i]
# print(diff)

min_value = diff[0]
min_index = 0
for i in range(number_of_elements):
    if diff[i] < min_value:
        min_value = diff[i]
        min_index = i
print(f'ближайший по значению элемент = {random_list[min_index]}')
