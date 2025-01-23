#criar uma classe chamada circulo que possua um atributo 
#para armazenar o raio e métodos para  calcular a
#area e o perimetro do circulo

class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def area_circulo(self):
        return 3.14 * self.raio **2

    def perimetro_circulo(self):
        return 2 * 3.14 * self.raio

        ##criar sempre um objeto de uma classe para testar se funcionar tudo certo
meu_circulo =  Circulo(6)
print(meu_circulo.perimetro_circulo())
