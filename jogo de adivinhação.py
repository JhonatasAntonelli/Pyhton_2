print ('-*-' * 10, 'Bem vindo ao jogo da adivinhação', '-*-' * 10)
import random
placar = 0
x = random.randint(1,11)
jogador = int(input('Tente adivinhar qual o número o computador escolheu, digite um número de 0-10: '))

while jogador != x and jogador != 0:
    x = random.randint(1, 11)
    print ('Você errou')
    jogador = int(input('Tente adivinhar qual o número o computador escolheu, digite um número de 1-10. Para sair so jogo digite 0: '))
    placar = placar + 1
    print('-*-' * 10, 'Próxima jogada', '-*-' * 10)
if jogador == 0:
    print ('Você saiu do jogo')
    print('-*-' * 10, 'Fim', '-*-' * 10)
if jogador == x:
    print ('Você acertou')
    print ('Fim de jogo, o placar foi {}'.format(placar))
    print ('-*-' * 10, 'Fim', '-*-' * 10)
