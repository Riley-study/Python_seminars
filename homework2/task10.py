# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное
# число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите
# минимальное количество монет, которые нужно перевернуть

from random import randint
randint(0, 1)
coins_number = int(input("введите количество монет: "))
count = 1
count_zero = 0
count_eagle = 0
while count <= coins_number:
    next_coins = randint(0, 1)
    if next_coins == 0:
        count_zero += 1
    else:
        count_eagle += 1
    count += 1
    print(next_coins)

if count_zero <= count_eagle:
    print(f'нужно перевернуть минимум {count_zero} шт')
else:
    print(f'нужно перевернуть минимум {count_eagle} шт')
