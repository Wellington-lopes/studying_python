# > DICIONÁRIOS

# Criando dicionário

dicionario = {}
dicionario = dict()

dicionario = {'name': 'Wellington', 'age': 32, 'height': 1.72}

print(dicionario['name'])
print(dicionario['age'])

#Adicionando elementos no dicionário

dicionario['programador'] = True
print(dicionario)

#Iterando sobre um dicionário

for chave in dicionario:
    print(chave, dicionario[chave])

#Testando a existência de uma chave

print('peso' in dicionario)
print('age' in dicionario)


