# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

number_n = int(input("Введите размер n: "))
number_m = int(input("Введите размер m: "))
number_k = int(input("Введите количество долек, которые необходимо отломить (k): "))

if number_k % number_n == 0 and number_k < number_n*number_m:
    print("yes")
elif number_k % number_n == 0 and number_k < number_n*number_m:
    print("yes")
else:
    print("no")
