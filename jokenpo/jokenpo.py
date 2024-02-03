from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0, 2)

print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')

while True:
    jogador = input('Qual é a sua jogada? ')
    
    if jogador.isdigit() and int(jogador) in [0, 1, 2]:
        jogador = int(jogador)
        break
    else:
        print("Por favor, digite um número válido (0, 1 ou 2).")

print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('OU...')
sleep(1)
print('TESOURA!')
sleep(2)
print('-=' * 11)

print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')

elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
