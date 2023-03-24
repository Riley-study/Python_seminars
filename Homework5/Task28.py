# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#    4

num_a = int(input("Enter number A: "))
num_b = int(input("Enter number B: "))


def summ(a, b) -> int:
    if a < b:
        b, a = a, b
    if a == 0:
        return 0
    return 1 + summ(a-1, b)


print(summ(num_a, num_b))
