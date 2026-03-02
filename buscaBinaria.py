'''#Exemplo.1
lista = [5, 2, 9, 1, 7]

lista_ordenada = sorted(lista)
print(lista_ordenada)

#Exemplo.2

ordenada = sorted(lista, reverse=True)
print(ordenada)

#Exemplo.3
numeros = [5, 2, 9, 1, 7]
numeros.sort(reverse=True)
print(numeros)
'''
#########################################################

#cria função com 4 parametros: array, x, low, high

#low = primeiro da lista
#high = low + 1
#lista = contém os valores
#x = alvo


def busca_binaria (lista, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if lista[mid] == x:
            return mid
        elif lista[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return 'Alvo não existe'

lista_nova = [3,4,5,6,7,8,9]
alvo = 6
l = 0
h = len(lista_nova)-1
resultado = busca_binaria(lista_nova, alvo, l, h)

if resultado != -1:
    print('Elmento está presente no index:' + str(resultado))
else:
    print('Elemento não encontrado')
