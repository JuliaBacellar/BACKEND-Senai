class Produto:
    def __init__(self, id_produto, nome, preco):
        self.id_produto = id_produto
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []
        self.total = 0

    def adicionar_produto(self, produto, quantidade):
        self.itens.append({"produto": produto, "quantidade": quantidade})
        self.total += produto.preco * quantidade

    def aplicar_desconto(self, percentual):
        self.total -= self.total * (percentual / 100)

    def calcular_frete(self, distancia):
        taxa_frete = 0.1
        frete = (distancia // 100) * taxa_frete * self.total
        return frete

    def calcular_total(self, distancia, desconto=0):
        if desconto > 0:
            self.aplicar_desconto(desconto)
        frete = self.calcular_frete(distancia)
        return self.total + frete

class Cliente:
    def __init__(self, id_cliente, nome):
        self.id_cliente = id_cliente
        self.nome = nome
        self.historico_compras = []

    def adicionar_compra(self, pedido):
        self.historico_compras.append(pedido)

    def recomendar_produtos(self):
        recomendacoes = []
        for compra in self.historico_compras:
            for item in compra.carrinho.itens:
                if item["produto"] not in recomendacoes:
                    recomendacoes.append(item["produto"])
        return recomendacoes

class Pedido:
    def __init__(self, cliente, carrinho, distancia, desconto=0):
        self.cliente = cliente
        self.carrinho = carrinho
        self.distancia = distancia
        self.desconto = desconto
        self.total = self.carrinho.calcular_total(distancia, desconto)
        self.cliente.adicionar_compra(self)

    def exibir_pedido(self):
        print(f"Pedido para {self.cliente.nome}")
        for item in self.carrinho.itens:
            print(f"{item['quantidade']} x {item['produto'].nome} - R$ {item['produto'].preco:.2f}")
        print(f"Total da compra: R$ {self.total:.2f}")
        print(f"Frete: R$ {self.carrinho.calcular_frete(self.distancia):.2f}")
        print(f"Desconto aplicado: {self.desconto}%")

produto1 = Produto(1, "Camiseta", 50.0)
produto2 = Produto(2, "Calça Jeans", 120.0)
produto3 = Produto(3, "Tênis", 150.0)

cliente1 = Cliente(1, "João Silva")

carrinho_cliente1 = Carrinho()
carrinho_cliente1.adicionar_produto(produto1, 2)
carrinho_cliente1.adicionar_produto(produto2, 1)

pedido1 = Pedido(cliente1, carrinho_cliente1, distancia=200, desconto=10)

pedido1.exibir_pedido()

recomendacoes = cliente1.recomendar_produtos()
print("Produtos recomendados com base em suas compras anteriores:")
for produto in recomendacoes:
    print(f"- {produto.nome}")
