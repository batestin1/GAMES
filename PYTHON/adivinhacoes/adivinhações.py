Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>>  JOGO DE ADIVINHAÇÃO
# DESENVOLVIDO POR MAYCON BATESTIN

import random

tentativachute = 0

print ('VAMOS ADIVINHAR?')
print ('')
print ('')
print ('Qual é seu nome:')
nome = input ()

number = random.randint(1, 10)
print (nome, 'Estou pensando em um número entre 1 e 10. Você sabe qual é?')

while tentativachute < 6:
    print ('Tente adivinhar?')
    tentativa = input()
    tentativa = int(tentativa)

    tentativachute = tentativachute + 1

    if tentativa < number:
        print ('Seu número é muito baixo')

    if tentativa > number:
        print ('Seu número é muito alto')

    if tentativa == number:
        break
if tentativa == number:
    tentativachute = str(tentativachute)
    print ('Bom trabalho!', nome, 'você acertou!')
if tentativa != number:
    tentativachute = str (tentativachute)
    print ('Não. Você errou o número.')



