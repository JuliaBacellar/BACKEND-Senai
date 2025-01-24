##crie uma classe chamada "funcionario" com atributos para armazenar o nome,
#o salario e o cargo do funcionario.
##Implemente métodos para calcular o salário líquido considerando descontos 
#de imposto e beneficios 

class Funcionario:
  def __init__(self,nome, salario, cargo_funcionario):
    self.nome = nome
    self.salario = salario
    self.cargo_funcionario = cargo_funcionario
    
  
  def salario_liquido(self):
    descontos_gerais = self.salario * 0.097
    salario_liquido =  self.salario - descontos_gerais 
    return salario_liquido

  
julia_funcionaria = Funcionario("julia",9000,"frontend")

print (julia_funcionaria.salario_liquido())