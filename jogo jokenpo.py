import random
print ('-*-'*10, 'Bom vindo ao jogo jokenpô', '-*-'*10)

pedra = 1
papel = 2
tesoura = 3
w = 0
z = 0
x = random.randint(1,3)
jogador = 1
while jogador !=0:
    x = random.randint(1,3)
    jogador = int(input('Para escolher: Pedra ({}) digite 1, Papel ({}) digite 2, Tesoura ({})digite 3 e para sair digite 0: '.format("\U0000270A", "\U0001F590", "\U0000270C")))
    if x == 1 and jogador == 1 :
        print ("Computador {}\n"
               "jogador {}". format("\U0000270A", "\U0000270A"))
        print ('O jogo empatou')
    if x == 1 and jogador == 2:
        print ("Computador {}\n"
               "jogador {}". format("\U0000270A", "\U0001F590"))
        print ('O jogador ganhou')
        w = w + 1
    if x == 1 and jogador == 3:
        print ("Computador {}\n"
               "jogador {}". format("\U0000270A", "\U0000270C"))
        print ('O Computador ganhou')
        z = z + 1
    if x == 2 and jogador == 2:
        print ("Computador {}\n"
               "jogador {}". format("\U0001F590", "\U0001F590"))
        print ('O jogo empatou')
    if x == 2 and jogador == 3:
        print ("Computador {}\n"
               "jogador {}". format("\U0001F590", "\U0000270C"))
        print ('O jogador ganhou')
        w = w + 1
    if x == 2 and jogador == 1:
        print ("Computador {}\n"
               "jogador {}". format("\U0001F590", "\U0000270A"))
        print ('O Computador ganhou')
        z = z + 1
    if x == 3 and jogador == 3:
        print ("Computador {}\n"
               "jogador {}". format("\U0000270C", "\U0000270C"))
        print ('O jogo empatou')
    if x == 3 and jogador == 1:
        print ("Computador {}\n"
               "jogador {}". format("\U0000270C", "\U0000270A"))
        print ('O jogador ganhou')
        w = w + 1
    if x == 3 and jogador == 2:
        print ("Computador {}\n"
               "jogador {}". format("\U0000270C", "\U0001F590"))
        print ('O Computador ganhou')
        z = z + 1
    if jogador == 0:
        print ('Fim de jogo, o jogador ficou com {} pontos e o computador com {} pontos'.format(w, z))
        print('-*-' * 9, 'Obrigado por jogar jokenpô comigo', '-*-' * 9)
        break
    print('O jogo está: {} para o jogador e {} para o computador'.format(w, z))
    print('-*-' * 29)
