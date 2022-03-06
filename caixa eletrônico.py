valor = int(input('Digite o valor que desja sacar: '))
cinquenta = 0
vinte = 0
dez = 0
um = 0
while valor >= 50:
    valor = valor - 50
    cinquenta += 1
while valor >= 20:
    valor = valor - 20
    vinte += 1
while valor >= 10:
    valor = valor -10
    dez += 1
while valor >= 1:
    valor = valor -1
    um += 1
print (f'Você vai receber {cinquenta} notas de R$50, {vinte} notas de R$20, {dez} notas de R$10 e {um} notas de 1R$')