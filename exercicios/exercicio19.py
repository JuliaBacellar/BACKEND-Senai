import random

class JogoAdivinhacao:
    def __init__(self, limite_inferior=1, limite_superior=100):
        self.limite_inferior = limite_inferior
        self.limite_superior = limite_superior
        self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior)
        self.tentativas = 0

    def fazer_palpite(self, palpite):
        self.tentativas += 1
        if palpite < self.numero_secreto:
            return "O número é maior."
        elif palpite > self.numero_secreto:
            return "O número é menor."
        else:
            return f"Parabéns! Você acertou o número em {self.tentativas} tentativa(s)."

    def reiniciar_jogo(self):
        self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior)
        self.tentativas = 0
        return "Jogo reiniciado! Tente adivinhar novamente."


jogo = JogoAdivinhacao()


print(jogo.fazer_palpite(50))  
print(jogo.fazer_palpite(75))  


print(jogo.reiniciar_jogo())


print(jogo.fazer_palpite(30)) 