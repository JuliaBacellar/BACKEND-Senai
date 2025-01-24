##implemente uma classe chamada "aluno" que possua atributos para armazenar o nome, a matricula e as notas de um aluno.Adicione métodos para
##calcular a média das notas e verificar a situação do aluno (aprovado ou reprovado)

##criação da classe "aluno"
##atributos nome matricula notas 
##métodos para calcular a média das notas e verificar se foi aprovado ou reprovado 

class Aluno: 
  def __init__(self,nome,matricula,notas):
    self.nome = nome
    self.matricula = matricula
    self.notas = notas
    
  def calcular_media(self):
    ##sum é para somar ## len ver o tamanho da lista
    soma = 0
    for i in self.notas:
      soma += nota
    return soma / len(self.notas)
  
  def verificar_situacao(self): 
      media = self.calcular_media()
      return "aprovado"  if media >=6 else "reprovado"
    
    
aluno  = Aluno("julia" "34546", [7.0,5.5,6.0])
print(f"media: {aluno.calcular_media():.2f}")
print(f"situação:{aluno.verificar_situacao()}")
      
    