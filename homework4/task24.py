# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены
# только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте
# выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random

user_number = int(input("введите количество кустов:"))

blackberry_bushes = [random.randint(1, 10) for _ in range(user_number)]
print(blackberry_bushes)

max_summ = 0
summ = 0
for i in range(1, len(blackberry_bushes)-1):
    summ = blackberry_bushes[i-1] + blackberry_bushes[i] + blackberry_bushes[i+1]
    if summ > max_summ:
        max_summ = summ
summ1 = blackberry_bushes[len(blackberry_bushes)-1] + blackberry_bushes[len(blackberry_bushes)-2] + blackberry_bushes[0]
summ2 = blackberry_bushes[len(blackberry_bushes)-1] + blackberry_bushes[1] + blackberry_bushes[0]


if summ1 > max_summ:
    max_summ = summ1
elif summ2 > max_summ:
    max_summ = summ1
print(max_summ)