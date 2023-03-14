# 17th: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи,
# выведите число -1.
# 0 1 1 2 3 5 8 12
user_number = int(input("Введите число > 1: "))

index = 3
fibonacciElement_1 = 1
fibonacciElement_0 = 1

while fibonacciElement_1 < (user_number+1):
    if user_number == fibonacciElement_1:
        print(index)
        break
    else:
        temp = fibonacciElement_1
        fibonacciElement_1 = fibonacciElement_1+fibonacciElement_0
        fibonacciElement_0 = temp
        index += 1
if fibonacciElement_1 > user_number:
    print(-1)




