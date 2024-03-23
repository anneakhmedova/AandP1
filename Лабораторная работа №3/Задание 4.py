from random import randint
i=0
k=0
while i<3:
    a = randint(1, 20)
    b = randint(1, 20)
    c = a+b
    d = str(a) + '+' + str(b) + '='
    e=int(input(d))
    if e==c:
        i=i
        k+=1
        print('Правильно')
    else:
        i+=1
        print('Не правильный ответ')
if i==3:
    print('Игра окончена. Правильных ответов:',k)