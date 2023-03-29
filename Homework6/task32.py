# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

input_min_max = list(map(int, input("введите минимальный и максимальный размер диапазона через пробел: ").split()))
var_min = input_min_max[0]
var_max = input_min_max[1]

initial_list = [random.randint(1, 10) for _ in range(10)]
print(initial_list)

result_list = []
count = 0
for item in initial_list:
    if var_min <= item <= var_max:
        result_list.append(initial_list.index(item, count))
    count += 1
print(result_list)
