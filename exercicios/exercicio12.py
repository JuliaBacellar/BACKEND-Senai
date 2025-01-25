class LojaVirtual:
    def __init__(self):
        self.produtos = {}
        self.carrinho = []

    def cadastrar_produto(self, nome, preco):
        self.produtos[nome] = preco
        return f"Produto '{nome}' cadastrado com sucesso por R$ {preco:.2f}."

    def adicionar_ao_carrinho(self, nome, quantidade):
        if nome not in self.produtos:
            return "Produto não encontrado."
        self.carrinho.append({"nome": nome, "quantidade": quantidade, "preco": self.produtos[nome]})
        return f"{quantidade} unidade(s) de '{nome}' adicionada(s) ao carrinho."

    def aplicar_desconto(self, percentual):
        for item in self.carrinho:
            item["preco"] -= item["preco"] * (percentual / 100)
        return f"Desconto de {percentual}% aplicado ao carrinho."

    def calcular_total(self):
        total = sum(item["preco"] * item["quantidade"] for item in self.carrinho)
        return f"Total da compra: R$ {total:.2f}"


loja = LojaVirtual()


print(loja.cadastrar_produto("Camiseta", 59.90))
print(loja.cadastrar_produto("Tênis", 199.90))

print(loja.adicionar_ao_carrinho("Camiseta", 2))
print(loja.adicionar_ao_carrinho("Tênis", 1))


print(loja.aplicar_desconto(10))


print(loja.calcular_total())
