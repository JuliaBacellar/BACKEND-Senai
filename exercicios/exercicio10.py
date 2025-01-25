class Livro:
    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return f"O livro '{self.titulo}' foi emprestado com sucesso."
        return f"O livro '{self.titulo}' já está emprestado."

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            return f"O livro '{self.titulo}' foi devolvido com sucesso."
        return f"O livro '{self.titulo}' já está disponível na biblioteca."

    def verificar_disponibilidade(self):
        return f"Disponível: {'Sim' if self.disponivel else 'Não'}"


livro1 = Livro("1984", "George Orwell", 328)


print(livro1.verificar_disponibilidade()) 


print(livro1.emprestar())  

print(livro1.emprestar())  


print(livro1.devolver()) 


print(livro1.verificar_disponibilidade())  