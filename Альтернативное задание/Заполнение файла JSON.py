import random
a = {
    'Азербайджан': 'Баку',
    'Италия': 'Рим',
    'Китай': 'Пекин',
    'Россия': 'Москва',
    'Япония': 'Токио'
}
with open('4.json','w', encoding='utf-8') as f:
    f.write(json.dumps(a,indent=4, ensure_ascii=False))
