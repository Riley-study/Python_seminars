# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
import random
import string

my_list = ''.join([random.choice(string.ascii_letters) for i in range(30)])
print(my_list)
my_dict = {}

for char in my_list:
    my_dict[char] = my_dict.get(char, 0) + 1
    if my_dict[char] > 1:
        print(f'{char}_{my_dict[char]}', end=" ")
    else:
        print(f'{char}', end=" ")


# input_string = "34343434343121212hhhvvv"
# dict1 = {}
# for i in input_string:
#     if i in dict1:
#         print(f"{i}_{dict1[i]}", end=" ")
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
#         print(i, end=" ")

#
# my_list = list(input_string)
# print(my_list)
#
# my_dict = dict()
# for i in set(my_list):
#     my_dict.setdefault(i, 0)
# print(my_dict)
#
# for key, value in my_dict.items():
#     for i in range(len(my_list)):
#         if my_list[i] == key:
#             if value > 0:
#                 my_list[i] = f'{key}_{value}'
#             value += 1
#
# result_str = ''
# for i in my_list:
#     result_str += f'{i} '
#
# print(result_str)

