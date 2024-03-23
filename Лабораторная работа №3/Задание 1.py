n=int(input('Введите количество строк:'))
i=0
b=''
while i<n:
    a=input('Введите слово:')
    b=str(b)+' '+str(a)
    i+=1
print(b)