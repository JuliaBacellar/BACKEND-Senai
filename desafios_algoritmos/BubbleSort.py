#algoritmo bubblesort organiza uma lista examinando cada conjunto de elementos 
#próximos na string,da esquerda para a direita,trocando suas posições se estiverem fora de ordem
#comparando repetidamente elementos próximos

def bubblesort(lista1): 
    
    for i in range(0,len(lista1)-1): 
        for j in range(len(lista1)-1): 
            if(lista1[j]>lista1[j+1]): 
                temp = lista1[j] 
                lista1[j] = lista1[j+1] 
                lista1[j+1] = temp 
    return lista1 
 
lista1 = [5, 3, 8, 6, 7, 2] 
print( lista1) 

print( bubblesort(lista1))  