##crie uma classe chamada retangulo que possua atributos para 
##armazenar a largura e a altura.Implemente métodos para calcular
##a área e o perimetro do retangulo


#criar uma classe retangulo
#atributos largura e altura 
#método calcular a area -> (passar o parametro area?) calculo area ->
#area = base * altura  
#calcular perimetro 
#Perímetro do retângulo: Perímetro=Lado1+Lado2+Lado3+Lado4
#criar um objeto que armazene a area
#criar um objeto que armazene o perimetro
#criar um objeto que armazene os dois para chamar 

class Retangulo:
  def __init__(self,largura,altura):
    self.largura = largura
    self.altura = altura
  
  def calcular_area(self):
    return self.largura * self.altura 
    
  def calcular_perimetro(self):
     return  2 * (self.largura + self.altura)
    
meu_retangulo = Retangulo(58,76)

area = meu_retangulo.calcular_area()
perimetro = meu_retangulo.calcular_perimetro()


print(f"a area do meu retangulo é {area}")
print(f"o perimetro do meu retangulo é {perimetro}")
