class Paciente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.historico_consultas = []

    def adicionar_consulta(self, data, especialidade, medico):
        consulta = {
            "data": data,
            "especialidade": especialidade,
            "medico": medico
        }
        self.historico_consultas.append(consulta)
        print(f"Consulta adicionada: {data} - {especialidade} com Dr(a). {medico}")

    def exibir_consultas(self):
        if not self.historico_consultas:
            print(f"{self.nome} ainda não possui consultas registradas.")
            return
        
        print(f"Histórico de consultas de {self.nome}:")
        for i, consulta in enumerate(self.historico_consultas, start=1):
            print(f"{i}. Data: {consulta['data']}, Especialidade: {consulta['especialidade']}, Médico: {consulta['medico']}")

paciente1 = Paciente("João Silva", 30)
paciente1.adicionar_consulta("2025-01-20", "Cardiologia", "Maria Oliveira")
paciente1.adicionar_consulta("2025-01-22", "Dermatologia", "Carlos Santos")
paciente1.exibir_consultas()
