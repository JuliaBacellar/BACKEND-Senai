class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.emprestimos = {}

    def cadastrar_livro(self, titulo, autor, quantidade):
        if titulo in self.livros:
            self.livros[titulo]["quantidade"] += quantidade
        else:
            self.livros[titulo] = {"autor": autor, "quantidade": quantidade}
        return f"Livro '{titulo}' de {autor} cadastrado com {quantidade} cópias."

    def verificar_disponibilidade(self, titulo):
        if titulo not in self.livros:
            return f"O livro '{titulo}' não está disponível na biblioteca."
        disponibilidade = self.livros[titulo]["quantidade"]
        if disponibilidade > 0:
            return f"O livro '{titulo}' está disponível. {disponibilidade} cópias restantes."
        return f"O livro '{titulo}' está indisponível no momento."

    def emprestar_livro(self, titulo, usuario):
        if titulo not in self.livros:
            return f"O livro '{titulo}' não está disponível na biblioteca."
        if self.livros[titulo]["quantidade"] > 0:
            self.livros[titulo]["quantidade"] -= 1
            if usuario not in self.emprestimos:
                self.emprestimos[usuario] = []
            self.emprestimos[usuario].append(titulo)
            return f"Livro '{titulo}' emprestado para {usuario}."
        return f"O livro '{titulo}' está indisponível no momento."

    def devolver_livro(self, titulo, usuario):
        if usuario not in self.emprestimos or titulo not in self.emprestimos[usuario]:
            return f"{usuario} não possui o livro '{titulo}' emprestado."
        self.livros[titulo]["quantidade"] += 1
        self.emprestimos[usuario].remove(titulo)
        return f"Livro '{titulo}' devolvido por {usuario}."

    def listar_livros(self):
        if not self.livros:
            return "Não há livros cadastrados na biblioteca."
        lista = []
        for titulo, info in self.livros.items():
            lista.append(f"'{titulo}' de {info['autor']} - {info['quantidade']} cópias disponíveis")
        return "\n".join(lista)


biblioteca = Biblioteca()

print(biblioteca.cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", 5))
print(biblioteca.cadastrar_livro("Harry Potter", "J.K. Rowling", 3))


print(biblioteca.verificar_disponibilidade("O Senhor dos Anéis"))
print(biblioteca.verificar_disponibilidade("Harry Potter"))
print(biblioteca.verificar_disponibilidade("Dom Quixote"))


print(biblioteca.emprestar_livro("O Senhor dos Anéis", "João"))
print(biblioteca.emprestar_livro("Harry Potter", "Maria"))
print(biblioteca.emprestar_livro("O Senhor dos Anéis", "Carlos"))


print(biblioteca.devolver_livro("O Senhor dos Anéis", "João"))
print(biblioteca.devolver_livro("Harry Potter", "Maria"))


print(biblioteca.listar_livros())
