import random

number = random.randint(1, 3)

numero_escolhido = int( input('Escolha um número de 1 a 3: ') )

while numero_escolhido != number:
    print('Você errou!')
    print('Tente novamente.')

    numero_escolhido = int( input('Escolha um número de 1 a 3: ') )

print('Você acertou!')