from time import sleep
from random import choice
from random import randint
computador = randint(1,10)
computador2 = randint(1,100)
computador3 = randint(1,50)
title = 'O GRANDE PENSADOR!'




print('-=-'*200)
print("{0:^80}".format(title))
print('-=-'*200)
nome = str(input('NOME DO JOGADOR: '))
print('-=-'*200)
dificuldade = int(input("""ESCOLHA O NÍVEL DE DIFICULDADE:
[ 1 ] FÁCIL
[ 2 ] MÉDIO
[ 3 ] DIFÍCIL
ESCOLHA: """))
print('-=-'*200)
if dificuldade == 1:
    sleep(1)
    print('Eu sou O GRANDE PENSADOR')
    sleep(1)
    print('E estou pensando em um número de 0 a 10')
    sleep(1)
    print('Será que você sabe qual é?')
    print('==-'*200)
    sleep(1)
    decisao1 = int(input("""ESTÁ PRONTO PARA COMEÇAR? 
    [ 1 ] SIM
    [ 2 ] NÃO
    R: """))
    sleep(1)
    if decisao1 == 1:
        acertou = False
        palpites = 0
        while not acertou:
            print('{} seu palpite é... '.format(nome))
            palpites += 1
            sleep(1)
            jogador = int(input('DIGITE UM NÚMERO: '))
            if jogador == computador:
                acertou = True
                print('-=-'*200)
            else:
                if jogador < computador:
                    sleep(1)
                    print('A DICA É... UM NUMERO MAIOR!')
                    print('-=-'*200)
                elif jogador > computador:
                    sleep(1)
                    print('A DICA É... UM NUMERO MENOR')
                    print('-=-'*200)
        print('Parabéns {}!'.format(nome))
        print('Você acertou em {} tentativas. Parabéns!'.format(palpites))
    else:
        sleep(1)
        print('-=-'*200)
        sleep(1)
        print('Tudo bem! Quem sabe na próxima vez, né?')
        sleep(1)
        print('FIM DE JOGO')
elif dificuldade == 2:
    sleep(1)
    print('Eu sou O GRANDE PENSADOR')
    sleep(1)
    print('E estou pensando em um número de 0 a 50')
    sleep(1)
    print('Será que você sabe qual é?')
    print('==-' * 200)
    sleep(1)
    decisao1 = int(input("""ESTÁ PRONTO PARA COMEÇAR? 
        [ 1 ] SIM
        [ 2 ] NÃO
        R: """))
    sleep(1)
    if decisao1 == 1 :
        acertou = False
        palpites = 0
        while not acertou :
            print('{} seu palpite é... '.format(nome))
            palpites += 1
            sleep(1)
            jogador = int(input('DIGITE UM NÚMERO: '))
            if jogador == computador3 :
                acertou = True
                print('-=-' * 200)
            else :
                if jogador<computador3 :
                    sleep(1)
                    print('A DICA É... UM NUMERO MAIOR!')
                    print('-=-' * 200)
                elif jogador>computador3:
                    sleep(1)
                    print('A DICA É... UM NUMERO MENOR')
                    print('-=-' * 200)
        print('Parabéns {}!'.format(nome))
        print('Você acertou em {} tentativas. Parabéns!'.format(palpites))
    else :
        sleep(1)
        print('-=-' * 200)
        sleep(1)
        print('Tudo bem! Quem sabe na próxima vez, né?')
        sleep(1)
        print('FIM DE JOGO')
elif dificuldade == 3:
    sleep(1)
    print('Eu sou O GRANDE PENSADOR')
    sleep(1)
    print('E estou pensando em um número de 0 a 100')
    sleep(1)
    print('Será que você sabe qual é?')
    print('==-' * 200)
    sleep(1)
    decisao1 = int(input("""ESTÁ PRONTO PARA COMEÇAR? 
        [ 1 ] SIM
        [ 2 ] NÃO
        R: """))
    sleep(1)
    if decisao1 == 1 :
        acertou = False
        palpites = 0
        while not acertou :
            print('{} seu palpite é... '.format(nome))
            palpites += 1
            sleep(1)
            jogador = int(input('DIGITE UM NÚMERO: '))
            if jogador == computador2 :
                acertou = True
                print('-=-' * 200)
            else :
                if jogador<computador2 :
                    sleep(1)
                    print('A DICA É... UM NUMERO MAIOR!')
                    print('-=-' * 200)
                elif jogador>computador2:
                    sleep(1)
                    print('A DICA É... UM NUMERO MENOR')
                    print('-=-' * 200)
        print('Parabéns {}!'.format(nome))
        print('Você acertou em {} tentativas. Parabéns!'.format(palpites))
    else :
        sleep(1)
        print('-=-' * 200)
        sleep(1)
        print('Tudo bem! Quem sabe na próxima vez, né?')
        sleep(1)
        print('FIM DE JOGO')