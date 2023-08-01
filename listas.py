lista = [10, 50, 30, 20, 100, 200]

"""for elemento in lista:
    print(elemento)

for i in range(len(lista)):
    print(i)
    print(lista[i])"""

#Metodos de Lista - append (add um elemento no final da minha lista)
lista.append(300)

print('Depois do append', lista)


#Insert (add um elemento em qualquer posição da minha lista)

lista.insert(2, 10)

print('Depois do insert', lista)

#Extend(Junta duas listas)
lista2 = [1, 2, 3, 4]

lista.extend(lista2)

print('Depois do extend', lista)

#Pop (Remove elementos da lista)

lista.pop()
lista.pop(0)

print('Depois do pop', lista)

#Remove (Remove os elementos especificos da lista)

lista.remove(100)
print('Depois do remove', lista)

# Count (Contar quantas vezes um elemento aparece na lista)

print('Quantidade de 20 na lista', lista.count(20))

# Index (Mostra um indice de um elemento na lista)

print('Index do 20 na lista', lista.index(20))

# Sort (Ordenar minha lista)

lista.sort()
#lista.sort(reverse=True)
print('Lista ordenada', lista)

# FUNÇÕES PARA LISTAS

#LEN
print(len(lista))

#SUM
print(sum(lista))

#MAX
print(max(lista))

#MIN
print(min(lista))