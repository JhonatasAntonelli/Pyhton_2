print('-*-'*5, 'Bom dia!', '-*-'*5)
numero = int(input('Digite um número para ser convertido'))
escolha = int(input('Digite 1 para converter para numero binário, 2 para octal e 3 para hexadecimal'))
if escolha == 1:
    print(bin(numero))
elif escolha == 2:
    print(oct(numero))
elif escolha == 3:
    print(hex(numero))
print('-*-'*5, 'Bom dia!', '-*-'*5)