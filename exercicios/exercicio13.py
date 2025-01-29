##Implemente uma classe chamada “Agenda” que represente uma agenda telefônica. 
# Essa classe deve permitir adicionar, editar e remover contatos, 
# além de buscar por contatos a partir de um nome ou número de telefone

class Agenda:
    def __init__(self):
        # Inicia a agenda com um dicionário vazio 'contatos', onde o telefone é a chave e o nome é o valor
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        # Verifica se o telefone já está cadastrado
        if telefone in self.contatos:
            return f"Telefone {telefone} já cadastrado."
        # Se não estiver, adiciona o nome e o telefone no dicionário
        self.contatos[telefone] = nome
        return f"Contato '{nome}' com telefone {telefone} adicionado com sucesso."

    def editar_contato(self, telefone, novo_nome, novo_telefone):
        # Se o telefone não existir na agenda, não pode editar
        if telefone not in self.contatos:
            return f"Contato com telefone {telefone} não encontrado."
        
        # Se encontrado, exclui o antigo e adiciona o novo nome e telefone
        del self.contatos[telefone]
        self.contatos[novo_telefone] = novo_nome
        return f"Contato atualizado: {novo_nome} com telefone {novo_telefone}."

    def remover_contato(self, telefone):
        # Se o telefone não existir, não pode remover
        if telefone not in self.contatos:
            return f"Contato com telefone {telefone} não encontrado."
        # Se existir, remove o contato
        del self.contatos[telefone]
        return f"Contato com telefone {telefone} removido com sucesso."

    def buscar_contato(self, nome=None, telefone=None):
        # Se passou um nome, procura o contato pelo nome
        if nome:
            for tel, cont_nome in self.contatos.items():
                if cont_nome.lower() == nome.lower():
                    return f"Contato encontrado: {cont_nome} - {tel}"
            return "Contato não encontrado."
        # Se passou um telefone, procura pelo telefone
        if telefone:
            if telefone in self.contatos:
                return f"Contato encontrado: {self.contatos[telefone]} - {telefone}"
            return "Contato não encontrado."
        # Se não passar nem nome nem telefone, pede pra informar um dos dois
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
