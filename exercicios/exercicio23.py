class Categoria:
    def __init__(self, nome):
        self.nome = nome

class Tarefa:
    def __init__(self, titulo, descricao, categoria, prioridade, data_vencimento):
        self.titulo = titulo
        self.descricao = descricao
        self.categoria = categoria
        self.prioridade = prioridade
        self.data_vencimento = data_vencimento
        self.status = "pendente"
    
    def editar(self, titulo=None, descricao=None, categoria=None, prioridade=None, data_vencimento=None):
        if titulo:
            self.titulo = titulo
        if descricao:
            self.descricao = descricao
        if categoria:
            self.categoria = categoria
        if prioridade:
            self.prioridade = prioridade
        if data_vencimento:
            self.data_vencimento = data_vencimento

    def concluir(self):
        self.status = "concluída"

    def iniciar(self):
        self.status = "em andamento"

    def __str__(self):
        return f"Título: {self.titulo}, Prioridade: {self.prioridade}, Status: {self.status}, Vencimento: {self.data_vencimento}, Categoria: {self.categoria.nome}"

class GerenciadorDeTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, titulo, descricao, categoria, prioridade, data_vencimento):
        tarefa = Tarefa(titulo, descricao, categoria, prioridade, data_vencimento)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
        else:
            for tarefa in self.tarefas:
                print(tarefa)
    
    def excluir_tarefa(self, titulo):
        tarefa = self.encontrar_tarefa(titulo)
        if tarefa:
            self.tarefas.remove(tarefa)
            print(f"Tarefa '{titulo}' excluída.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")

    def editar_tarefa(self, titulo, **dados):
        tarefa = self.encontrar_tarefa(titulo)
        if tarefa:
            tarefa.editar(**dados)
            print(f"Tarefa '{titulo}' editada.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")

    def encontrar_tarefa(self, titulo):
        for tarefa in self.tarefas:
            if tarefa.titulo == titulo:
                return tarefa
        return None

    def filtrar_por_status(self, status):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if tarefa.status == status]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(tarefa)
        else:
            print(f"Nenhuma tarefa com status '{status}' encontrada.")

    def filtrar_por_prioridade(self, prioridade):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if tarefa.prioridade == prioridade]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(tarefa)
        else:
            print(f"Nenhuma tarefa com prioridade '{prioridade}' encontrada.")

    def filtrar_por_data_vencimento(self, data_vencimento):
        tarefas_filtradas = [tarefa for tarefa in self.tarefas if tarefa.data_vencimento == data_vencimento]
        if tarefas_filtradas:
            for tarefa in tarefas_filtradas:
                print(tarefa)
        else:
            print(f"Nenhuma tarefa com vencimento em '{data_vencimento}' encontrada.")

categoria1 = Categoria("Desenvolvimento")
categoria2 = Categoria("Pessoal")

gerenciador = GerenciadorDeTarefas()

gerenciador.adicionar_tarefa("Finalizar projeto", "Concluir o desenvolvimento da aplicação", categoria1, "Alta", "2025-01-30")
gerenciador.adicionar_tarefa("Fazer compras", "Comprar mantimentos para a casa", categoria2, "Média", "2025-01-25")

gerenciador.listar_tarefas()

gerenciador.editar_tarefa("Fazer compras", descricao="Comprar mantimentos para a casa e para o trabalho", prioridade="Alta")
gerenciador.listar_tarefas()

gerenciador.filtrar_por_status("pendente")

gerenciador.excluir_tarefa("Finalizar projeto")
gerenciador.listar_tarefas()
