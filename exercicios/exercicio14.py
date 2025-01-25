class MaquinaDeVendas:
    def __init__(self):
        self.produtos = {}
        self.estoque = {}
        self.dinheiro_inserido = 0

    def cadastrar_produto(self, nome, preco, quantidade):
        self.produtos[nome] = preco
        self.estoque[nome] = quantidade
        return f"Produto '{nome}' cadastrado com sucesso por R$ {preco:.2f}, quantidade: {quantidade}."

    def selecionar_produto(self, nome):
        if nome not in self.produtos:
            return f"Produto '{nome}' não encontrado na máquina."
        if self.estoque[nome] == 0:
            return f"Produto '{nome}' está fora de estoque."
        return f"Produto '{nome}' selecionado. Preço: R$ {self.produtos[nome]:.2f}. Quantidade disponível: {self.estoque[nome]}."

    def inserir_dinheiro(self, valor):
        self.dinheiro_inserido += valor
        return f"R$ {valor:.2f} inserido(s). Total inserido: R$ {self.dinheiro_inserido:.2f}"

    def realizar_compra(self, nome):
        if nome not in self.produtos:
            return f"Produto '{nome}' não encontrado."
        preco = self.produtos[nome]
        if self.estoque[nome] == 0:
            return f"Produto '{nome}' fora de estoque."
        if self.dinheiro_inserido < preco:
            return f"Dinheiro insuficiente. Faltam R$ {preco - self.dinheiro_inserido:.2f}."
        
        self.estoque[nome] -= 1
        troco = self.dinheiro_inserido - preco
        self.dinheiro_inserido = 0
        return f"Compra realizada com sucesso! Troco: R$ {troco:.2f}."

    def retornar_estoque(self):
        estoque_info = "\n".join([f"{nome}: {quantidade} unidades" for nome, quantidade in self.estoque.items()])
        return f"Estoque disponível:\n{estoque_info}"


maquina = MaquinaDeVendas()


print(maquina.cadastrar_produto("Coca-Cola", 5.00, 10))
print(maquina.cadastrar_produto("Chips", 3.50, 5))

print(maquina.selecionar_produto("Coca-Cola"))
print(maquina.selecionar_produto("Chips"))

print(maquina.inserir_dinheiro(10.00))


print(maquina.realizar_compra("Coca-Cola"))

print(maquina.retornar_estoque())
