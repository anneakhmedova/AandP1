a=''
b=''
while a!='stop':
    a=input('Введите слово:')
    b=str(b)+' '+str(a)

print(b.replace('stop',''))