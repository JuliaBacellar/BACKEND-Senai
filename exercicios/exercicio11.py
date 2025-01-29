#Implemente uma classe chamada “Banco” que represente uma instituição financeira.
#Essa classe deve conter métodos para cadastrar clientes, 
#abrir contas bancárias e realizar operações como saques, depósitos e transferências
class Banco:
    def __init__(self):
        # Aqui a gente cria um dicionário 'clientes' que vai armazenar os dados dos clientes
        # E outro dicionário 'contas' que vai armazenar os saldos das contas
        self.clientes = {}  
        self.contas = {}

    def cadastrar_cliente(self, nome, cpf):
        # Primeiro, a gente verifica se o CPF já está cadastrado no dicionário de clientes
        if cpf in self.clientes:
            # Se o CPF já existir, a função retorna que o cliente já foi cadastrado
            return f"Cliente com CPF {cpf} já cadastrado."
        # Se o CPF não existir, a gente cadastra o cliente no dicionário com o nome dele
        self.clientes[cpf] = {"nome": nome}
        # Retorna uma mensagem dizendo que o cliente foi cadastrado com sucesso
        return f"Cliente {nome} cadastrado com sucesso."

    def abrir_conta(self, cpf, saldo_inicial=0):
        # Verifica se o cliente já foi cadastrado. Se não, pede para cadastrar primeiro
        if cpf not in self.clientes:
            return f"CPF {cpf} não encontrado. Cadastre o cliente primeiro."
        # Verifica se o cliente já tem uma conta, se sim, não pode abrir outra
        if cpf in self.contas:
            return f"O cliente {self.clientes[cpf]['nome']} já possui uma conta."
        # Se o cliente não tiver conta, a gente cria a conta dele com o saldo inicial (se não passar, o saldo é 0)
        self.contas[cpf] = saldo_inicial
        # Retorna uma mensagem dizendo que a conta foi aberta com o saldo inicial
        return f"Conta aberta para {self.clientes[cpf]['nome']} com saldo inicial de R$ {saldo_inicial:.2f}."

    def consultar_saldo(self, cpf):
        # Se o CPF não tem uma conta, a função retorna que a conta não foi encontrada
        if cpf not in self.contas:
            return "Conta não encontrada."
        # Se a conta existir, ela mostra o saldo atual da conta
        return f"Saldo atual: R$ {self.contas[cpf]:.2f}"

    def depositar(self, cpf, valor):
        # Se o CPF não tiver uma conta, retorna "Conta não encontrada"
        if cpf not in self.contas:
            return "Conta não encontrada."
        # Se o valor do depósito for menor ou igual a zero, não deixa fazer o depósito
        if valor <= 0:
            return "O valor do depósito deve ser maior que zero."
        # Se o valor for válido, o valor é adicionado ao saldo da conta
        self.contas[cpf] += valor
        # Retorna que o depósito foi realizado com sucesso
        return f"Depósito de R$ {valor:.2f} realizado com sucesso."

    def sacar(self, cpf, valor):
        # Se o CPF não tiver uma conta, retorna "Conta não encontrada"
        if cpf not in self.contas:
            return "Conta não encontrada."
        # Se o valor do saque for menor ou igual a zero, não deixa fazer o saque
        if valor <= 0:
            return "O valor do saque deve ser maior que zero."
        # Se o saldo for suficiente, o valor é subtraído do saldo da conta
        if self.contas[cpf] >= valor:
            self.contas[cpf] -= valor
            # Retorna que o saque foi realizado com sucesso
            return f"Saque de R$ {valor:.2f} realizado com sucesso."
        # Se o saldo for insuficiente, retorna uma mensagem de erro
        return "Saldo insuficiente."

    def transferir(self, cpf_origem, cpf_destino, valor):
        # Ve se as contas de origem e destino existem
        if cpf_origem not in self.contas:
            return "Conta de origem não encontrada."
        if cpf_destino not in self.contas:
            return "Conta de destino não encontrada."
        # Ve se o valor da transferência é maior que zero
        if valor <= 0:
            return "O valor da transferência deve ser maior que zero."
        # Se o saldo da conta de origem for suficiente, transfere o valor entre as contas
        if self.contas[cpf_origem] >= valor:
            self.contas[cpf_origem] -= valor
            self.contas[cpf_destino] += valor
            # Retorna que a transferência foi realizada com sucesso.
            return f"Transferência de R$ {valor:.2f} realizada com sucesso."
        # Se o saldo for insuficiente, retorna uma mensagem de erro.
        return "Saldo insuficiente para transferência."



banco = Banco()

print(banco.cadastrar_cliente("Ana Costa", "36349"))
print(banco.cadastrar_cliente("Carlos Mendes", "3456"))

print(banco.abrir_conta("5474", saldo_inicial=800))
print(banco.abrir_conta("4674", saldo_inicial=500))

print(banco.consultar_saldo("7960"))

print(banco.depositar("4234", 300))

print(banco.sacar("4567", 200))

print(banco.transferir("85678", "18965", 100))

print(banco.consultar_saldo("456"))
print(banco.consultar_saldo("6"))
