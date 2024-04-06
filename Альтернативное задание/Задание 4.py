import json
with open('4.json', 'r', encoding='utf-8') as f:
    d = json.load(f)
a = input('Введите страну:')
b = input('Введите столицу:')
if a in d:
    print("Такая страна и столица уже есть")
else:
    print('1.Страна-Столица, 2.Столица-Страна')
    c=int(input('Какой вариант добавления?'))
    if c==1:
        d[a]=b
    elif c==2:
        d[b]=a
    else:
        print('Ошибка')



with open('4.json', 'w',encoding='utf-8') as f:
    json.dump(d, f, indent=4, ensure_ascii=False)