# Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит планет
# найдет ту, по которой вращается самая далекая планета. Круговые орбиты не учитывайте: вы знаете, что у вашей звезды
# таких планет нет, зато искусственные спутники были были запущены на круговые орбиты. Результатом функции должен быть
# кортеж, содержащий длины полуосей эллипса орбиты самой далекой планеты. Каждая орбита представляет из себя кортеж из
# пары чисел - полуосей ее эллипса. Площадь эллипса вычисляется по формуле S = piab, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка: проще всего будет найти эллипс в два шага: сначала
# вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь. Гарантируется, что самая
# далекая планета ровно одна.

import random
import math

half_os1 = [random.randint(5, 10) for item in range(10)]
# print(half_os1)
half_os2 = [random.randint(5, 10) for item in range(10)]
# print(half_os2)
list_of_orbits = list(zip(half_os1, half_os2))
print(list_of_orbits)


def filter_list_of_orbit(initial_list):
    new_list = list(filter(lambda x: x[0] != x[1], initial_list))
    mult_list = list(map(lambda x: math.pi * x[0] * x[1], new_list))
    index = mult_list.index(max(mult_list))
    print(new_list)
    print(list(map(int, mult_list)))
    print(f'самая далекая планета вращается по эллипсу с полуосями: {new_list[index]}')

list_of_orbits = filter_list_of_orbit(list_of_orbits)

