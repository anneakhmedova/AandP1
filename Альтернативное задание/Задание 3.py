def f1():
    a = input('Введите страну:')
    b = input('Введите столицу:')
    with open('3.txt') as f:
        if a in f.read():
            print("Такая страна и столица уже есть")
        else:
            print('1.Страна-Столица, 2.Столица-Страна')
            c = int(input('Какой вариант добавления?'))
            if c == 1:
                d = a + " " + b
            elif c == 2:
                d = b + " " + a
            else:
                print('Ошибка')
            with open("3.txt", 'a') as f:
                f.write(d + '\n')
def f2():
    f = open('3.txt', 'r')
    d = f.read()
    print(d)
print('1. Добавить страну-стоицу')
print('2. Показать содержимое')
c=int(input('Выберите вариант:'))
if c==1:
    f1()
elif c==2:
    f2()
else:
    print('Такого варианта нет')