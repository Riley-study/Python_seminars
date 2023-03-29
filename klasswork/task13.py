# Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая
# само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары
# дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k. Пары
# необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).
import time

numb_k = 3000
list_delit = []
for i in range(1, numb_k):
    count = 0
    for item in range(1, i//2+1):
        if i % item == 0:
            count += item
    list_delit.append(count)
# print(list_delit)
# print(list_delit[219], list_delit[283])

dict_friends_number = {}

for item in range(1, numb_k-1):
    for i in range(1, numb_k-1):
        if list_delit[item-1] == i and list_delit[i-1] == item and i != item:
            dict_friends_number[item] = dict_friends_number.get(item, i)
            # print(f'дружественная пара чисел {list_delit[item-1]}, {list_delit[i-1]}')

list_pair = []
for key, value in dict_friends_number.items():
    if (value, key) not in list_pair:
        list_pair.append((key, value))
        print(key, value)
