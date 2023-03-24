# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым


def func(number):
    n = 0
    for i in range(1, number+1):
        if number % i == 0:
            n += 1
    if n > 2:
        print(f"{number} not simple")
    else:
        print(f"{number} simple")


print(func(47))
