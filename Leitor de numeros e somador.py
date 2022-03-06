numero = int(input('Digite um número para ser somado, para encerrar a soma digite 999: '))
soma = 0
x = 0
while numero != 999:
    soma = numero + soma
    numero = int(input('Digite um número para ser somado, para encerrar a soma digite 999: '))
    x = x + 1
print('A soma dos números deu {} e você digitou {} números'.format(soma, x))