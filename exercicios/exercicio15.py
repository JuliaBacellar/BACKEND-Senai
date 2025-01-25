class JogoCartas:
    def __init__(self, jogadores):
        self.jogadores = jogadores
        self.cartas = [
            f"{cor}{numero}" for cor in ['Vermelho', 'Azul', 'Verde', 'Amarelo'] 
            for numero in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Reversa', 'Pular', 'Coringa']
        ]
        self.carta_atual = None
        self.baralho = []
        self.mesa = []

    def embaralhar_cartas(self):
        # Embaralhamento manual das cartas
        for i in range(len(self.cartas) - 1, 0, -1):
            j = i - 1  # Índice de troca
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]
        self.baralho = self.cartas.copy()
        return "Cartas embaralhadas com sucesso."

    def distribuir_cartas(self):
        if not self.baralho:
            return "Baralho vazio. Não é possível distribuir cartas."
        
        cartas_por_jogador = 7
        self.jogadores_cartas = {jogador: [] for jogador in self.jogadores}
        for jogador in self.jogadores:
            for _ in range(cartas_por_jogador):
                carta = self.baralho.pop()
                self.jogadores_cartas[jogador].append(carta)

        return "Cartas distribuídas para os jogadores."

    def iniciar_jogo(self):
        if not self.baralho:
            return "Baralho vazio. Não é possível iniciar o jogo."
        
        self.carta_atual = self.baralho.pop()
        self.mesa.append(self.carta_atual)
        return f"Jogo iniciado! Primeira carta na mesa: {self.carta_atual}"

    def jogar_carta(self, jogador, carta):
        if jogador not in self.jogadores_cartas:
            return f"Jogador {jogador} não encontrado."
        
        if carta not in self.jogadores_cartas[jogador]:
            return f"{jogador} não tem a carta {carta}."
        
        if not self.pode_jogar(carta):
            return f"A carta {carta} não pode ser jogada sobre a carta atual {self.carta_atual}."
        
        self.jogadores_cartas[jogador].remove(carta)
        self.mesa.append(carta)
        self.carta_atual = carta
        return f"{jogador} jogou a carta {carta}."

    def pode_jogar(self, carta):
        cor_carta, numero_carta = carta.split()[0], carta.split()[1]
        cor_mesa, numero_mesa = self.carta_atual.split()[0], self.carta_atual.split()[1]

        return cor_carta == cor_mesa or numero_carta == numero_mesa or numero_carta == 'Coringa'

    def exibir_mesa(self):
        return f"Carta atual na mesa: {self.carta_atual}"

    def exibir_cartas(self, jogador):
        if jogador not in self.jogadores_cartas:
            return f"Jogador {jogador} não encontrado."
        return f"Cartas de {jogador}: {', '.join(self.jogadores_cartas[jogador])}"



jogo = JogoCartas(jogadores=["João", "Maria", "Pedro"])


print(jogo.embaralhar_cartas())


print(jogo.distribuir_cartas())


print(jogo.iniciar_jogo())


print(jogo.jogar_carta("João", "Vermelho 1"))
print(jogo.jogar_carta("Maria", "Azul 3"))
print(jogo.jogar_carta("Pedro", "Vermelho 3"))


print(jogo.exibir_mesa())
print(jogo.exibir_cartas("João"))
