# 17th: 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики
#  за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам
# в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках располагается
# N целых чисел. Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат
# в диапазоне от –50 до 50


from random import randint
randint(-3, 3)
weather = 0
user_number = int(input("Введите количество дней для проверки: "))
count_all_days = 0
count_warm_days = 0
max_warm_days = 0

while count_all_days < user_number:
    weather = weather + randint(-3, 3)
    if weather > 0:
        count_warm_days += 1
    elif count_warm_days > max_warm_days:
        max_warm_days = count_warm_days
        count_warm_days = 0
    else:
        count_warm_days = 0
    count_all_days += 1
    print(f'{count_all_days} : {weather}')
else:
    if count_all_days == user_number and count_warm_days > max_warm_days:
       max_warm_days = count_warm_days

print(f'максимальное количество теплых дней подряд : {max_warm_days}')


