## linked list,algoritmo de ordenação 
##divide o problema grande em problemas pequenos 
##depois juntar esses pedaços pequenos em ordem crescente formando uma organização

#<--exemplo--> 
# [9,4,5,2,6,8]
# [9,4,5] [2,6,8]
# [9,4][5] [2] [6,8]
# [9] [4] [5] [2] [6] [8]

#terminando a divisão , juntar os numeros em ordem crescente
# [4] [9]
# [2] [5]
# [6] [8]

#agora juntamos as listas 
# [4,9] e [2,5] --> [2,4,5,9]
# [6,8] -->[6,8]

#agora juntar tudo
#[2,4,5,9] e [6,8] --> [2,4,5,6,8,9]

#<-- pronto temos uma lista ordenada --> 

#como funciona o merge sort e implemente o algoritmo merge sort sem utilizar funções 
#ou bibliotecas prontas 
#usei recursão
#encontrar o meio e mergear 

lista = [2,5,9,4,3]
#quando acontece a divisão dos arrays se for trabalhar com a direita a esquerda fingir que nao existe 
#e viceversa
#criou a função mergesort com parametro lista 
def mergesort(lista):
    #se len(ve o tamanho da lista) for menor ou igual a 1 
    if len(lista) <= 1:
        #vai retornar a lista 
        return lista
    meio = len (lista)//2 
    left = lista[0:meio]
    right = lista[meio:]

    #armazeno os valores ja encontrados nas variaveis chama mergesort recursivamente para dividir e ordenar as sublistas
    left = mergesort(left)
    right = mergesort(right)

    #variavel i e j que são temporarias para controlar e percorrer o right e left 
    i, j = 0, 0
    resultado = []

    # Combina as duas listas ordenadas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    # Adiciona os elementos restantes de left (se houver)
    while i < len(left):
        resultado.append(left[i])
        i += 1

    # Adiciona os elementos restantes de right (se houver)
    while j < len(right):
        resultado.append(right[j])
        j += 1
#cuidado com a identação
    return resultado

    
print(mergesort(lista))

#def teste():
#    import random
#   i = random.randint(0,15)
#    print(i)
#    if i == 5 :
#        return 
#    teste()
#    print(i)


#teste()