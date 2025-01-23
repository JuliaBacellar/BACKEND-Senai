#implemente uma classe chamada "ContaBancaria" que possua atributos
#para armazenar o numero da conta,nome do titular e saldo
#adicione métodos para realizar depósitos e saques

class ContaBancaria:
    def __init__(self,numero_conta,nome_titular,saldo):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo 
    #
    def deposito_cliente(self, valor):
        print(f"voce vai depositar {valor}")





contaju = ContaBancaria(132, "ju", -550)

contaju.deposito_cliente(145)

