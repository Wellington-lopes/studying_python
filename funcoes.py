#Função recebendo nome sem parâmetro
"""def saudacao():
    print('Seja bem vindo')
    name = input('Digite seu nome: ')
    print('Olá, é um prazer ter você fazendo parte desse canal: ', name)

saudacao()"""

#Função recebendo nome com parâmetro

"""def saudacao(name, curso):
    print(f'Seja bem vindo, {name}')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao('Wellington', 'Python')"""

#Função recebendo nome com parâmetro default

"""def saudacao(name, curso='Python'):
    print(f'Seja bem vindo, {name}')
    print(f'Olá, é um prazer ter você fazendo parte desse curso de {curso}')

saudacao('Wellington')"""

#Função com retorno

"""def soma(num1, num2):
    return num1 + num2

resultado = soma(5, 6)

print(resultado)"""

def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
       return num1 + num2
    elif operacao == '-':
       return num1 - num2
    elif operacao == 'x':
       return num1 * num2
    elif operacao == '/':
       return num1 / num2

resultado = calculadora(10, 5, 'x')

print(resultado)
