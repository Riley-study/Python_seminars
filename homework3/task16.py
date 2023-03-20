# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

import random
number_of_elements = int(input("введите количество элементов в массиве: "))
random_list = [random.randint(1, 10) for _ in range(number_of_elements)]
print(random_list)

count_element = int(input("количество каких элементов нужно почитать? "))
count = 0
for i in range(number_of_elements):
    if random_list[i] == count_element:
        count += 1

print(f'элемент {count_element} встречается в массиве {count} раз(а).')
