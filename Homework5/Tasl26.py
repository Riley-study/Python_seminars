# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

num_a = int(input("Enter number A: "))
num_b = int(input("Enter number B: "))


def degree_func(a, b) -> int:
    if b == 1:
        return a
    result = a * degree_func(a, b-1)
    return result


print(degree_func(num_a, num_b))
