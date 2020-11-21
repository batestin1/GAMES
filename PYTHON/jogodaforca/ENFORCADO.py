import random
from time import sleep

title = 'O ENFORCADO!'
print('-=-' * 200)
print('{0:^80}'.format(title))
print('-=-' * 200)
l1 = 'Este é o jogo do enforcado'
print('{0:^80}'.format(l1))
sleep(1)
l2 = 'Escolha as letras com cuidado'
print('{0:^80}'.format(l2))
sleep(1)
l3 = 'Senão, você vai se dar mal!'
print('{0:^80}'.format(l3))
print('-=-' * 200)

nomeJogador = str(input('Nome do Jogador: '))
print('-=-' * 200)

modalidade = int(input("""Escolha o tema e boa sorte!
[ 1 ] CINEMA
[ 2 ] FRUTAS
[ 3 ] CIDADES
[ 4 ] OBJETOS
R: """))

if modalidade == 1 :
    cinema = []
    with open('cinema.txt', 'r') as f :
        cinema = f.readlines()
    indice_cinema = random.randint(0, len(cinema) - 1)
    sorteio1 = cinema[indice_cinema].replace('\n', '')
    cinema = ['_'] * len(sorteio1)
    V = 0
    while True :

        letra = str(input('Digite uma letra: ')).upper()
        V += 1

        for i in range(len(sorteio1)) :

            if letra == sorteio1[i] :
                cinema[i] = letra

        if ''.join(cinema) == sorteio1 :

            print(f'{nomeJogador} parabéns! Você acertou a palavra é {sorteio1}.')
            if V<=10 :
                print(f'E você só precisou de {V} tentativas para isso!')

            elif V>10 :
                print(f'Nossa, mas você gastou {V} tentativas para isso!')
                sleep(1)
                print('Tá fraco, hein!')

            break

        else :
            print(''.join(cinema))
elif modalidade == 2 :
    frutas = []
    with open('frutas.txt', 'r') as f:
        frutas = f.readlines()
        indice_frutas = random.randint(0, len(frutas) - 1)
        sorteio2 = frutas[indice_frutas].replace('\n', '')
        frutas = ['_'] * len(sorteio2)
        V = 0
        while True :

            letra = str(input('Digite uma letra: ')).upper()
            V += 1

            for i in range(len(sorteio2)) :

                if letra == sorteio2[i] :
                    frutas[i] = letra

            if ''.join(frutas) == sorteio2 :

                print(f'{nomeJogador} parabéns! Você acertou a palavra é {sorteio2}.')
                if V<=10 :
                    print(f'E você só precisou de {V} tentativas para isso!')

                elif V>10 :
                    print(f'Nossa, mas você gastou {V} tentativas para isso!')
                    sleep(1)
                    print('Tá fraco, hein!')

                break

            else :
                print(''.join(frutas))



elif modalidade == 3 :
    cidades = []
    with open('cidades.txt', 'r') as f:
        cidades = f.readlines()
        indice_cidades = random.randint(0, len(cidades) - 1)
        sorteio3 = cidades[indice_cidades].replace('\n', '')
        cidades = ['_'] * len(sorteio3)
        V = 0
        while True :

            letra = str(input('Digite uma letra: ')).upper()
            V += 1

            for i in range(len(sorteio3)) :

                if letra == sorteio3[i] :
                    cidades[i] = letra

            if ''.join(cidades) == sorteio3 :

                print(f'{nomeJogador} parabéns! Você acertou a palavra é {sorteio3}.')
                if V<=10 :
                    print(f'E você só precisou de {V} tentativas para isso!')

                elif V>10 :
                    print(f'Nossa, mas você gastou {V} tentativas para isso!')
                    sleep(1)
                    print('Tá fraco, hein!')

                break

            else :
                print(''.join(cidades))


elif modalidade == 4 :
    objetos = []
    with open('objetos.txt', 'r') as f :
        objetos = f.readlines()
        indice_objetos = random.randint(0, len(objetos) - 1)
        sorteio4 = objetos[indice_objetos].replace('\n', '')
        objetos = ['_'] * len(sorteio4)
        V = 0
        while True :

            letra = str(input('Digite uma letra: ')).upper()
            V += 1

            for i in range(len(sorteio4)) :

                if letra == sorteio4[i] :
                    objetos[i] = letra

            if ''.join(objetos) == sorteio4 :

                print(f'{nomeJogador} parabéns! Você acertou a palavra é {sorteio4}.')
                if V<=10 :
                    print(f'E você só precisou de {V} tentativas para isso!')

                elif V>10 :
                    print(f'Nossa, mas você gastou {V} tentativas para isso!')
                    sleep(1)
                    print('Tá fraco, hein!')

                break

            else :
                print(''.join(objetos))


