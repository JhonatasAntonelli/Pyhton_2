print('-=-' * 30)
print ('VAMOS JOGAR PAR OU IMPAR?')
print('-=-' * 30)
placar = 0
import random
while True:
    jogador = int(input('Qual número você escolhe? '))
    escolha = str(input('Você quer par ou impar (P/I)? ')).upper()
    computador = random.randint(0,10)
    soma = (jogador + computador) % 2
    if soma == 0 and escolha == 'P':
        placar = placar +1
        print (f'Você ganhou, o computador escolheo {computador}')
    if soma != 0 and escolha == 'I':
        placar = placar +1
        print(f'Você ganhou, o computador escolheo {computador}')
    if soma == 0 and escolha == 'I':
        print (f'Você perdeu, o placar foi {placar}')
        print (f'O computador escolheu {computador}')
        break
    if soma != 0 and escolha == 'P':
        print(f'Você perdeu, o placar foi {placar}')
        print(f'O computador escolheu {computador}')
        break