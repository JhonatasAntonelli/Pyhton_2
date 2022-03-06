print ('-' * 50)
numero = int(input('Digite um número para conhecer a tabuada dele: '))
print ('-' * 50)
x = 1
while x <= 10:
    if numero < 0:
        break
    tabuada = x * numero
    print (f'{x} X {numero} = {tabuada}')
    x += 1
    if x == 11:
        print ('-' * 50)
        numero = int(input('Digite um número para conhecer a tabuada dele: '))
        print('-' * 50)
        x = 1
