from random import randint
computador = randint(0, 5) #faz o computador 'PENSAR'
print('-=-' * 20)
print('vou pensar em um número, tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei ? '))# jogador tenta adivinhar 
if computador == jogador:
    print('PARABENS!!, Você acertou')
else:
    print('GANHEI! Eu pensei no número {} e não no número {}'.format(computador, jogador))