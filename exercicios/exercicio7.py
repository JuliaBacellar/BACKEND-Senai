#crie uma classe chamada "triangulo" com atributos para armazenar os tres lados do triangulo
#implemente métodos para verificar se é um triangulo válido e calcular sua area 
 class Triangulo:
    def __init__(self,altura_um,altura_dois,base):
        self.altura_um = altura_um
        self.altura_dois = altura_dois
        self.base = base


#é um triangulo valido se a soma de dois lados for maior que o terceiro lado
#calcular area triangulo -> area = base * altura / 2 
#ver se todas as combinações possíveis de soma de dois lados sendo maiores que o terceiro lado
    def triangulo_valido (self):
        if self.altura_um + self.altura_dois > self.base:
            return True
        else:
            return False

    def calcular_area(self):
        area_triangulo = self.base * (self.altura_um + self.altura_dois) /2
        return area_triangulo

testando_triangulo = Triangulo(32,54,67)

print(testando_triangulo.triangulo_valido())
print(testando_triangulo.calcular_area())

