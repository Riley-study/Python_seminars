# 0 1 1 2 3 5 8 13 21 34 55 86

user_numb = int(input("enter a number: "))


def fib(number):
    if number == 1 or number == 0:
        return number
    return fib(number-1) + fib(number-2)


print(fib(user_numb))
