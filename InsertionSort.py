#algoritmo insertion sort implementação
#comparando cada elemento com o anterior e inseridndo na posição correta
#usando loop para comparar valores anteriores

lista = [4,5,3,6,7,2]

def insertionsort(lista):
    for i in range(1,len (lista)):
        posição = lista[i]
        j = i - 1
        while j >=0 and lista[j] > posição:
            lista[j + 1] = lista[j]
            j-= 1
        lista[j+1] =posição

insertionsort(lista)
print(lista)