numero = int(input('Digite um númer: '))
soma = 0
digitos = 0
while numero != 999:
    soma = numero + soma
    numero = int(input('Digite um número: '))
    digitos += 1
    if numero == 999:
        break
print (f'A soma dos número digitados foi {soma} e foram digitados {digitos} números')