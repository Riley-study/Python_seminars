# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов
# нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

input_vars = list(map(int, input("введите первый эл-т последоват-ти, разность и кол-во эл-ов через пробел: ").split()))
# an = a1 + (n-1) * d.
var_a1 = input_vars[0]
var_d = input_vars[1]
var_n = input_vars[2]

result_list = []

for i in range(1, var_n):
    number = var_a1 + (i-1)*var_d
    result_list.append(number)

print(result_list)
