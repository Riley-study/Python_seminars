# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
import random
from random import randint

user_number = int(input('введите целое число: '))
shift_number = int(input('введите количество элементов для сдвига: '))

randint(0, 10)
new_list = [random.randint(0, 10) for _ in range(user_number)]
print(new_list)
# i = 0
# while i < shift_number:
#     new_list.insert(0, new_list[-1])
#     new_list.pop(-1)
#     i += 1
# print(new_list)
for i in range(shift_number):
    new_list.insert(0, new_list[-1])
    new_list.pop(-1)
print(new_list)

print(new_list[-shift_number:] + new_list[:-shift_number])

for i in range(len(new_list)):
    print(new_list[i - shift_number], end=' ')
