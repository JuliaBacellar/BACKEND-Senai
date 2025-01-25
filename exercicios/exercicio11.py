class Banco:
    def __init__(self):
        self.clientes = {}
        self.contas = {}

    def cadastrar_cliente(self, nome, cpf):
        if cpf in self.clientes:
            return f"Cliente com CPF {cpf} já cadastrado."
        self.clientes[cpf] = {"nome": nome}
        return f"Cliente {nome} cadastrado com sucesso."

    def abrir_conta(self, cpf, saldo_inicial=0):
        if cpf not in self.clientes:
            return f"CPF {cpf} não encontrado. Cadastre o cliente primeiro."
        if cpf in self.contas:
            return f"O cliente {self.clientes[cpf]['nome']} já possui uma conta."
        self.contas[cpf] = saldo_inicial
        return f"Conta aberta para {self.clientes[cpf]['nome']} com saldo inicial de R$ {saldo_inicial:.2f}."

    def consultar_saldo(self, cpf):
        if cpf not in self.contas:
            return "Conta não encontrada."
        return f"Saldo atual: R$ {self.contas[cpf]:.2f}"

    def depositar(self, cpf, valor):
        if cpf not in self.contas:
            return "Conta não encontrada."
        if valor <= 0:
            return "O valor do depósito deve ser maior que zero."
        self.contas[cpf] += valor
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."

    def sacar(self, cpf, valor):
        if cpf not in self.contas:
            return "Conta não encontrada."
        if valor <= 0:
            return "O valor do saque deve ser maior que zero."
        if self.contas[cpf] >= valor:
            self.contas[cpf] -= valor
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        return "Saldo insuficiente."

    def transferir(self, cpf_origem, cpf_destino, valor):
        if cpf_origem not in self.contas:
            return "Conta de origem não encontrada."
        if cpf_destino not in self.contas:
            return "Conta de destino não encontrada."
        if valor <= 0:
            return "O valor da transferência deve ser maior que zero."
        if self.contas[cpf_origem] >= valor:
            self.contas[cpf_origem] -= valor
            self.contas[cpf_destino] += valor
            return f"Transferência de R$ {valor:.2f} realizada com sucesso."
        return "Saldo insuficiente para transferência."


banco = Banco()

print(banco.cadastrar_cliente("Ana Costa", "12312312300"))
print(banco.cadastrar_cliente("Carlos Mendes", "32132132100"))

print(banco.abrir_conta("12312312300", saldo_inicial=800))
print(banco.abrir_conta("32132132100", saldo_inicial=500))

print(banco.consultar_saldo("12312312300"))

print(banco.depositar("32132132100", 300))

print(banco.sacar("12312312300", 200))

print(banco.transferir("32132132100", "12312312300", 100))

print(banco.consultar_saldo("12312312300"))
print(banco.consultar_saldo("32132132100"))
