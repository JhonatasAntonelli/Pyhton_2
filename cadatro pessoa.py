continuar = 'S'
maioridade = 0
homem = 0
mulher = 0
while continuar == 'S':
    idade = input('Digite a idade: ')
    while idade.isalpha():
        idade = input('Digite a idade: ')
    sexo = input('Digite o sexo M/F: ').upper()
    while sexo != 'F' and sexo != 'M':
        sexo = input('Digite o sexo M/F: ').upper()
    while sexo.isnumeric():
        sexo = input('Digite o sexo M/F: ').upper()
    if int(idade) > 18:
        maioridade += 1
    if sexo == 'M':
        homem += 1
    if int(idade) < 20 and sexo == 'F':
        mulher += 1
    continuar = input('Digite s para continuar e n para parar').upper()
    while continuar.isnumeric() and continuar != 'S' and continuar != 'N':
        continuar = input('Digite s para continuar e n para parar').upper()
    while continuar != 'S' and continuar != 'N':
        continuar = input('Digite s para continuar e n para parar').upper()
print (f'Temos {homem} homens, desses, {maioridade} possuem mais de 18 anos e temos {mulher} mulheres com mais de 20 anos')