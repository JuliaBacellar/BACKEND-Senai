class Calendario:
    def __init__(self, ano):
        self.ano = ano
        self.feriados = {}

    def adicionar_feriado(self, data, descricao):
       
        self.feriados[data] = descricao

    def exibir_calendario(self, mes):

        if mes < 1 or mes > 12:
            return "Mês inválido. Escolha um mês entre 1 e 12."
        
        dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            dias_por_mes[1] = 29  

        dias_do_mes = dias_por_mes[mes - 1]
        
        calendario_mes = f"Calendário de {mes}/{self.ano}:\n"
        primeiro_dia = self.calcular_primeiro_dia(mes) 
        calendario_mes += "Seg Ter Qua Qui Sex Sab Dom\n" 

     
        calendario_mes += "    " * primeiro_dia
        
        for dia in range(1, dias_do_mes + 1):
            calendario_mes += f"{dia:2} "
            if (primeiro_dia + dia) % 7 == 0:
                calendario_mes += "\n"

        return calendario_mes

    def calcular_primeiro_dia(self, mes):
        
        if mes < 3:
            mes += 12
            ano = self.ano - 1
        else:
            ano = self.ano
        
        k = ano % 100
        j = ano // 100
        h = (1 + (13 * (mes + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7

        return (h + 5) % 7  

    def verificar_feriado(self, data):
       
        if data in self.feriados:
            return f"{data} é feriado: {self.feriados[data]}"
        return f"{data} não é feriado."

    def diferenca_dias(self, data1, data2):
   
        dias_ano = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.ano % 4 == 0 and (self.ano % 100 != 0 or self.ano % 400 == 0):
            dias_ano[1] = 29  
        
        def data_para_dias(data):
            dia, mes = map(int, data.split('/'))
            dias = sum(dias_ano[:mes-1]) + dia
            return dias
        
        dias_data1 = data_para_dias(data1)
        dias_data2 = data_para_dias(data2)
        
        return abs(dias_data2 - dias_data1)


calendario = Calendario(2025)


calendario.adicionar_feriado("01/01", "Ano Novo")
calendario.adicionar_feriado("25/12", "Natal")
calendario.adicionar_feriado("07/09", "Independência do Brasil")


print(calendario.exibir_calendario(3))


print(calendario.verificar_feriado("01/01"))
print(calendario.verificar_feriado("15/04"))


print(calendario.diferenca_dias("01/01", "25/12"))
print(calendario.diferenca_dias("15/03", "01/01"))
