# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

input_string = "34343434343121212"

my_list = list(input_string)
print(my_list)

my_dict = dict()
for i in set(my_list):
    my_dict.setdefault(i, 0)
print(my_dict)

for key, value in my_dict.items():
    for i in range(len(my_list)):
        if my_list[i] == key:
            if value > 0:
                my_list[i] = f'{key}_{value}'
            value += 1

result_str = ''
for i in my_list:
    result_str += f'{i} '

print(result_str)

