# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве
# аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число
# строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

num_rows, num_columns = 6, 6

def print_operation_table(rows, columns):
    for i in range(1, rows+1):
        res_list = list()
        for j in range(1, columns + 1):
            res_list.append(i * j)
        print(*res_list)


print_operation_table(num_rows, num_columns)


def operation(x, y):
    list_a = [i for i in range(1, x+1)]
    for item in range(1, y+1):
        list_b = list(map(lambda c: c * item, list_a))
        print(*list_b)

operation(num_rows, num_columns)

# >>> a = [1, 2, 3, 4, 5, 6, 7]
# >>> b = list(map(lambda x: x**2, a))
# >>> print('a = {}\nb = {}'.format(a, b))
# a = [1, 2, 3, 4, 5, 6, 7]
# b = [1, 4, 9, 16, 25, 36, 49]