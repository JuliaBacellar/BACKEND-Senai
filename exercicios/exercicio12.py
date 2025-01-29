##Crie uma classe chamada “LojaVirtual” que represente uma plataforma de vendas online. 
# Essa classe deve ter funcionalidades para cadastrar produtos,
# gerar carrinho de compras, aplicar descontos e calcular o valor total da compra.
class LojaVirtual:
    def __init__(self):
        # Aqui a loja começa com um dicionário 'produtos' (vai guardar nome e preço) e uma lista 'carrinho' (pra colocar o que a galera comprar)
        self.produtos = {}
        self.carrinho = []

    def cadastrar_produto(self, nome, preco):
        # Quando o produto é cadastrado, ele entra no 'produtos' com o nome e o preço
        self.produtos[nome] = preco
        # Aí retorna uma mensagem dizendo que foi cadastrado com sucesso
        return f"Produto '{nome}' cadastrado com sucesso por R$ {preco:.2f}."

    def adicionar_ao_carrinho(self, nome, quantidade):
        # Se o produto não existir na loja, avisa que não achou
        if nome not in self.produtos:
            return "Produto não encontrado."
        # Se encontrou o produto, adiciona no carrinho com a quantidade e o preço
        self.carrinho.append({"nome": nome, "quantidade": quantidade, "preco": self.produtos[nome]})
        # Retorna uma mensagem dizendo quantos produtos foram adicionados
        return f"{quantidade} unidade(s) de '{nome}' adicionada(s) ao carrinho."

    def aplicar_desconto(self, percentual):
        # Aqui a gente aplica um desconto no preço de todos os produtos no carrinho
        for item in self.carrinho:
            item["preco"] -= item["preco"] * (percentual / 100)
        # Retorna a mensagem de que o desconto foi aplicado
        return f"Desconto de {percentual}% aplicado ao carrinho."

    def calcular_total(self):
        # Calcula o total somando o preço de cada produto multiplicado pela quantidade
        total = sum(item["preco"] * item["quantidade"] for item in self.carrinho)
        # Retorna o total da compra
        return f"Total da compra: R$ {total:.2f}"



loja = LojaVirtual()


print(loja.cadastrar_produto("Camiseta", 59.90))
print(loja.cadastrar_produto("Tênis", 199.90))

print(loja.adicionar_ao_carrinho("Camiseta", 2))
print(loja.adicionar_ao_carrinho("Tênis", 1))


print(loja.aplicar_desconto(10))


print(loja.calcular_total())
