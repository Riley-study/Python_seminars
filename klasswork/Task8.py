# Дана упорядоченная последовательность an чисел от 1 до N. Из копии данной последовательности bn удалили одно число,
# а оставшиеся перемешали. Найти удаленное число.
import random

user_number = int(input("введите целое число: "))
first_list = [i for i in range(user_number)]
print(first_list)

second_list = first_list.copy()
second_list.pop(random.randint(0, user_number+1))
random.shuffle(second_list)
print(second_list)

# 1 version
set1 = set(first_list)
set2 = set(second_list)
diff = set1.difference(set2)
print(*diff)

# 2 version
for item in first_list:
    if item not in second_list:
        print(item)
