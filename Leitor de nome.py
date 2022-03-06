idade_somada = 0
x = 0
z = 0
for c in range (0,4):
    nome = str(input('Qual o seu nome?'))
    idade = int(input('Digite a sua idade'))
    sexo = int(input('Digite 1 para masculino e 2 para feminino'))
    idade_somada = idade + idade_somada
    if sexo == 1:
        if idade > x:
            x = idade
            y = nome
    if sexo == 2:
        if idade < 20:
            z = 1 + z
print ('A média da idade de todos é', (idade_somada/4))
print ('O nome do homem mais velho é', y)
print ('{} mulheres possuem menos de 20 anos'.format(z))
