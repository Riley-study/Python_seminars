f = open('new_text.txt', 'w', encoding='UTF-8')
# открыли для записи и сразу создали файл
# (каждый раз перезаписывает файл с нуля)
f.write("приветствие, начнем разбираться\n")
f.write("пункт 1\n")
f.write("пункт 2 \nпункт 3")
f.close() # закрыли

f = open('new_text.txt', 'r', encoding='UTF-8')
# print(f.read())
# f.readlines()
# print(f.readlines()) # выведет все в одну строку
# print(f.read(7)) # выведет все красиво по строкам сначала первые 7 символов
# print(f.read(2)) #  затем следующие 2
# for line in f:
#     print(line)
f.close() # закрыли

f = open('new_text.txt', 'r+', encoding='UTF-8')
for line in f:
    if "пункт" in line:
        line = line.replace('пункт', 'стр')
        print(line)
        f.writelines(f'\n{line}')
f.close()

f1 = open('new_text_reserve.txt', 'w+', encoding='UTF-8')
f = open('new_text.txt', 'r', encoding='UTF-8')
data = f.readlines()
a = 'пункт'
for line in data:
    f1.writelines(f'\n{line}')
f.close()
f1.close()

f = open('new_text.txt', 'w', encoding='UTF-8')
f1 = open('new_text_reserve.txt', 'r', encoding='UTF-8')
data = f1.readlines()
for line in data:
    if a not in line:
        f.write(line)
f.close()
f1.close()
