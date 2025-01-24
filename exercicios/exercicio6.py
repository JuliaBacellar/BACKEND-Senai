#implemente uma classe chamada "produto" que possua atributos para armazenar
#o nome,preço e quantidade em estoque.Adicione métodos para calcular o valor
#total em estoque e verifique se o produto está disponível 

class Produto:
    def __init__(self,nome,preço,quantidade_estoque):
        self.nome = nome
        self.preço = preço ## valor unitario do produto
        self.quantidade_estoque = quantidade_estoque


#calcular valor total em estoque 
#verificar se o produto esta disponivel (<0 não disponivel)
    def valor_total(self):
        estoque_total = self.quantidade_estoque*self.preço
        return estoque_total

    #se esta disponivel 
    def esta_disponivel(self):
        if self.quantidade_estoque <= 0:
            return True
    
estoque_disponivel = Produto("acetona",32.40,3)

print(estoque_disponivel.valor_total())
print(estoque_disponivel.esta_disponivel())