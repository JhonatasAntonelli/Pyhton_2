frase = str(input("Digite uma frase ou palavras")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('A frase é um palindromo')
    print (inverso, junto)
else:
    print('A frase não é um palindromo')
    print(inverso, junto)