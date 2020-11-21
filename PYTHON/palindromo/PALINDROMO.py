from time import sleep



title = 'O PALÍNDROMO'
print('-=-'*300)
print('{0:^20}'.format(title))
print('-=-'*200)
sleep(1)
print('-=-'*200)
print('Panlídromos são toda palavra ou frase')
print('que pode ser lida de trás pra frente,')
print('e que independente da direção,')
print('o seu sentido.')
print('-=-'*200)
sleep(1)
decisao1 = int(input("""Você quer continuar?
[ 1 ] SIM
[ 2 ] NÃO
R: """))

while not decisao1 == 2:
    sleep(1)
    print('-=-'*200)

    frase = str(input('Digite uma palavra que queira analisar: ')).strip().upper()
    palavras = frase.split()
    junto = ''.join(palavras)
    inverso = ''

    for letra in range(len(junto) - 1, -1, -1):
        inverso += junto[letra]
    if inverso == junto:
        print(f'A palavra {frase} é um PALÍNDROMO, pois seu inverso é {inverso}')
        print('-=-'*200)

    else:
        print(f'A palavra {frase} não é um PALÍNDROMO, pois seu inverso é {inverso}')
        print('-=-'*200)

sleep(1)
print('-=-'*200)
print('FIM DE JOGO')
print('-=-'*200)