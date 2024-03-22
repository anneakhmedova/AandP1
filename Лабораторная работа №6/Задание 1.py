a = {
    'Италия': 'Рим',
    'Россия': 'Москва',
    'Китай': 'Пекин',
    'Япония': 'Токио',
    'Азербайджан': 'Баку'
}
def o():
    print(a)
def v():
    g1=a.get('Азербайджан')
    g2=a.get('Италия')
    g3=a.get('Китай')
    g4=a.get('Россия')
    g5=a.get('Япония')
    print('Страны :1-Азербайджан,2-Италия, 3-Китай,4-Россия,5-Япония')
    r=input("Выбирети страну:")
    if r=='1':
        b=g1
    elif r=='2':
        b=g2
    elif r=='3':
        b=g3
    elif r=='4':
        b=g4
    else:
        b=g5
    print(b)
def p():
    s=dict(sorted(a.items()))
    print(s)
print('1.Задание a')
print('2.Задание b')
print('3.Задание c')
n=int(input('Выберите номер задания:'))
if n==1:
    print(o())
elif n==2:
    print(v())
elif n==3:
    print(p())
else:
    print('Ошибка')