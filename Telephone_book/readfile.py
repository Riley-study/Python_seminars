print("проверка связи!!")

def show_all(a):
    file = open('sample1.txt', 'r', encoding='UTF-8')
    data = file.readlines()
    print(data)
    file.close()
