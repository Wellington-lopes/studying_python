"""for i in range(1, 6):
    print(i)"""
soma = 0
# media = 0
for i in range(1, 4):
    nota = float(input(f'Informe sua nota {i}: '))

    soma = soma + nota

print('Sua média é: ', soma / 3)


