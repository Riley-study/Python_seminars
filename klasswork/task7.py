# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших
# предыдущего (элемента с предыдущим номером)
from random import randint
randint(0, 50)

new_list = [randint(0, 10) for _ in range(10)]
print(new_list)

# version 1
count = 0
for i in range(len(new_list)-1):
    if new_list[i+1] > new_list[i]:
        count += 1
print(count)

# version 2
count_list = [i for i in range(1, len(new_list)) if new_list[i-1] < new_list[i]]
print(len(count_list))
