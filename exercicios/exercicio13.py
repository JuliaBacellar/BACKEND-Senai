class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        if telefone in self.contatos:
            return f"Telefone {telefone} já cadastrado."
        self.contatos[telefone] = nome
        return f"Contato '{nome}' com telefone {telefone} adicionado com sucesso."

    def editar_contato(self, telefone, novo_nome, novo_telefone):
        if telefone not in self.contatos:
            return f"Contato com telefone {telefone} não encontrado."
        
        del self.contatos[telefone]
        self.contatos[novo_telefone] = novo_nome
        return f"Contato atualizado: {novo_nome} com telefone {novo_telefone}."

    def remover_contato(self, telefone):
        if telefone not in self.contatos:
            return f"Contato com telefone {telefone} não encontrado."
        del self.contatos[telefone]
        return f"Contato com telefone {telefone} removido com sucesso."

    def buscar_contato(self, nome=None, telefone=None):
        if nome:
            for tel, cont_nome in self.contatos.items():
                if cont_nome.lower() == nome.lower():
                    return f"Contato encontrado: {cont_nome} - {tel}"
            return "Contato não encontrado."
        if telefone:
            if telefone in self.contatos:
                return f"Contato encontrado: {self.contatos[telefone]} - {telefone}"
            return "Contato não encontrado."
        return "Informe um nome ou telefone para buscar."


agenda = Agenda()


print(agenda.adicionar_contato("João Silva", "123456789"))
print(agenda.adicionar_contato("Maria Souza", "987654321"))


print(agenda.buscar_contato(nome="João Silva"))
print(agenda.buscar_contato(telefone="987654321"))


print(agenda.editar_contato("123456789", "João Silva", "111222333"))


print(agenda.remover_contato("987654321"))

print(agenda.buscar_contato(nome="Maria Souza"))
print(agenda.buscar_contato(telefone="123456789"))
