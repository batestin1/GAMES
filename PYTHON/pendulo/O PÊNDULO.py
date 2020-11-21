from time import sleep
from random import choice

A = 'sim, você sabe muito bem o que isso significa!'
B = 'não. Eu não acho isso certo!'
C = 'sim, pode ser que isso dê certo!'
D = 'não. Isso vai doer!'
E = 'sim, mas seria legal outra coisa.'
F = 'não. E nem me faça pensar muito'
G = 'sim, mas vai deixar marcas!'
H = 'não. Mas gostaria que fosse o contrário.'
I = 'sim, e eu recomendo muito!'
J = 'não, mas quem sou eu, né?'
L = 'sim, pode ter certeza que sim!'
M = 'não. Nem pensar!'
N = 'sim, e você vai não vai se arrepender!'
O = 'não! e fique em casa!'
P = 'sim! Sim! Sim! Definitivamente SIM'
Q = 'não. Eu não recomendo!'
R = 'sim, mas gostaria que fosse não'
S = 'não, e aprenda a respeitar a opinião dos outros'
T = 'sim, mas acho que fica melhor com chocolate!'
U = 'não, mas quem sabe amanhã, né?'
V = 'sim, e tenha certeza que você vai amar!'
X = 'não, e eu acho que você não sabe o que quer...'
Z = 'sim, e volte a dormir'

lista = [A,B,C,D,E,F,G,H,I,J,L,M,N,O,P,Q,R,S,T,U,V,X,Z]


Resposta = 'SIM'

print('-=-'*200)
Titulo = 'Este é o PÊNDULO!'
print("{0:^80}".format(Titulo))
print('-=-'*200)
sleep(1)
subtitulo = 'Faça uma pergunta ao PÊNDULO'
print("{0:^80}".format(subtitulo))
sleep(1)
subt2 = 'E obtenha uma resposta para sua vida!'
print("{0:^80}".format(subt2))
print('-=-'*200)
nome = str(input('Qual o seu nome? '))

while Resposta == "SIM":
    print('{}, '.format(nome))
    pergunta = str(input("faça sua pergunta: "))
    sleep(1)
    print('...')
    sleep(1)
    print('....processando...')
    sleep(1)
    print('......................processando...')
    sleep(1)
    print('...ops!')
    sleep(1)
    print('R: {}, {}'.format(nome, choice(lista)))
    print('-=-'*200)
    Resposta = str(input('Quer fazer outra pergunta? ')).upper()
    print('-=-'*200)
    sleep(1)
print('FIM DO JOGO')

                   