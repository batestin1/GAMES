from random import randint
from time import sleep
titles = 'LOTERICA BATESTIN'
print('-=-'*300)
print('{0:^80}'.format(titles))
print('-=-'*300)

e = int(input("""Qual jogo você deseja apostar
[ 1 ] Megasena
[ 2 ] Quina
[ 3 ] Lotofácil
R: """))

if e == 1:
    lista = list()
    jogos = list()
    print ('-=-'*30)
    print ('MEGASENA')
    print('-=-'*30)
    quant = int(input('Quantos jogos deseja fazer? '))
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1,60)
            if num not in lista:
                lista.append(num)
                cont +=1
            if cont >= 6:
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot +=1
    print('-=-'* 3, f'SORTEANDO {quant} JOGOS', '-=-'*3)
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}: {l}')
        sleep(1)
elif e == 2:
    lista = list()
    jogos = list()
    print('-=-' * 30)
    print('QUINA')
    print('-=-' * 30)
    quant = int(input('Quantos jogos deseja fazer? '))
    tot = 1
    while tot<=quant :
        cont = 0
        while True :
            num = randint(1, 80)
            if num not in lista :
                lista.append(num)
                cont += 1
            if cont>=5 :
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-=-' * 3, f'SORTEANDO {quant} JOGOS', '-=-' * 3)
    for i, l in enumerate(jogos) :
        print(f'Jogo {i + 1}: {l}')
        sleep(1)
elif e==3:
    lista = list()
    jogos = list()
    print('-=-' * 30)
    print('LOTOFÁCIL')
    print('-=-' * 30)
    quant = int(input('Quantos jogos deseja fazer? '))
    tot = 1
    while tot<=quant :
        cont = 0
        while True :
            num = randint(1, 25)
            if num not in lista :
                lista.append(num)
                cont += 1
            if cont>=15 :
                break
        lista.sort()
        jogos.append(lista[:])
        lista.clear()
        tot += 1
    print('-=-' * 3, f'SORTEANDO {quant} JOGOS', '-=-' * 3)
    for i, l in enumerate(jogos) :
        print(f'Jogo {i + 1}: {l}')
        sleep(1)


