def binaria(l, a):
    baixo = 0
    alto = len(l) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        if l[meio] == a:
            return meio
        elif l[meio] < a:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

lista = [1, 3, 7]
alvo = 7
resultado = binaria(lista, alvo)

if resultado != -1:
    print("Achou no index", resultado)
else:
    print("Não achou")
