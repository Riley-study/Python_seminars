# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ_number = int(input("введите сумму чисел: "))
product_number = int(input("введите произведение чисел: "))

first_number = 0
second_number = 0
while first_number < summ_number:
    second_number = summ_number - first_number
    if first_number*second_number == product_number:
        print(f'первое число {first_number}, второе число {second_number}')
    first_number += 1

else:
    if first_number > summ_number:
        print("таких чисел не существует")

