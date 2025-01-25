#implemente uma classe chamada "carro" com atributos para armazenar a marca, o modelo
#e a velocidade atual do carro.Adicione métodos para acelerar(aumentar),
# frear(diminuir) e exibir a velocidade
#atual 

#velocidade atual pode ser float 

class Carro:
    def __init__ (self,marca_carro,modelo_carro,velocidade_atual):
        self.marca_carro = marca_carro
        self.modelo_carro = modelo_carro
        self.velocidade_atual = velocidade_atual

    #se o carro estiver mais de tal km frear 
    def acelerar_carro(self, valor=10):
        if self.velocidade_atual + valor > 200:
            self.velocidade_atual = 200
            print("vc atingiu a maxima velocidade")
        else:
            self.velocidade_atual += valor
            print(f"acelerando,velocidade atual:{self.velocidade_atual}km/h")

    def frear_carro(self, valor=10):
        if self.velocidade_atual - valor < 0:
            self.velocidade_atual = 0
            print("O carro parou completamente.")
        else:
            self.velocidade_atual -= valor
            print(f"Freando... Velocidade atual: {self.velocidade_atual} km/h")

    def exibir_velocidade(self):
        print(f"A velocidade atual é: {self.velocidade_atual} km/h")
        
carro1 = Carro("civic", "naosei", 50)
carro1.acelerar_carro(40)
carro1.frear_carro(30)
carro1.exibir_velocidade()         
