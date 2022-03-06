operacao = 1
while operacao != 8:
    x = int(input('Digite o primeiro número da operação matemática: '))
    y = int(input('Digite o primeiro número da operação matemática: '))
    operacao = int(input('Escolha a operação que você deseja: \n'
                         '[1] Multiplicar\n'
                         '[2] Ddividir\n'
                         '[3] Somar\n'
                         '[4] Subtrair\n'
                         '[5] Maior\n'
                         '[6] menor\n'
                         '[7] Digitar novos número \n'
                         '[8] Sair: '))
    if operacao == 1:
        print ('O resultado é', x * y)
    if operacao == 2:
        print('O resultado é', x / y)
    if operacao == 3:
        print('O resultado é', x + y)
    if operacao == 4:
        print('O resultado é', x - y)
    if operacao == 5:
        if x > y:
            print('O maior número é', x )
        if x < y:
            print('O maior número é', y )
    if operacao == 6:
        if x > y:
            print('O menor número é', y )
        if x < y:
            print('O menor número é', x )
    if operacao == 7:
        x = int(input('Digite o primeiro número da operação matemática'))
        y = int(input('Digite o primeiro número da operação matemática'))
        operacao = int(input('Escolha a operação que você deseja: \n'
                             '[1] Multiplicar\n'
                             '[2] Ddividir\n'
                             '[3] Somar\n'
                             '[4] Subtrair\n '
                             '[5] Maior\n '
                             '[6] menor\n '
                             '[7] Digitar novos número \n'
                             '[8] Sair'))
if operacao == 8:
    print ('Você saiu')