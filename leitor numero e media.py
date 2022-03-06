numero = int(input('Digite os números para enconrar a média: '))
soma = numero
x = 1
maior = numero
menor = numero
continuar = 'S'
while continuar == 'S':
    numero1 = int(input('Digite os números para enconrar a média: '))
    x = x + 1
    continuar = str(input('Para continuar a média, digite S e para terminar digite N: ')).upper()
    if numero1 > maior:
        maior = numero1
    if numero1 < menor:
        menor = numero1
    soma = numero1 + soma
if continuar == 'N':
    media = soma / x
    print('A media dos números deu {}, o menor número foi {} e o maior foi {}'.format(media, menor, maior))