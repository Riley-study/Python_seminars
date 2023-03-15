# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("введите число: "))
degree_of_2 = 1
while degree_of_2 <= number:
    print(degree_of_2)
    degree_of_2 *= 2
