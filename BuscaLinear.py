def busca(l, a):
    for i in range(len(l)):
        if l[i] == a:
            return i
    return -1

lista = [3, 7, 1]
alvo = 7
resultado = busca(lista, alvo)

if resultado != -1:
    print("Achou no index", resultado)
else:
    print("Não achou")
