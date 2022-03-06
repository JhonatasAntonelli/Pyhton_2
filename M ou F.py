sexo = 'p'
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite m para masculino e f para feminino')).upper()
if sexo == 'M' or sexo == 'F':
    print('FIM')
