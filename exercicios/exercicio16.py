class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = []
    
    def adicionar_usuario(self, nome):
        if nome in self.usuarios:
            return f"Usuário {nome} já existe."
        self.usuarios[nome] = {"amigos": [], "posts": []}
        return f"Usuário {nome} adicionado com sucesso."
    
    def adicionar_amigo(self, usuario1, usuario2):
        if usuario1 not in self.usuarios or usuario2 not in self.usuarios:
            return "Um dos usuários não existe."
        if usuario2 in self.usuarios[usuario1]["amigos"]:
            return f"{usuario1} e {usuario2} já são amigos."
        self.usuarios[usuario1]["amigos"].append(usuario2)
        self.usuarios[usuario2]["amigos"].append(usuario1)
        return f"{usuario1} e {usuario2} agora são amigos."

    def publicar_mensagem(self, usuario, mensagem):
        if usuario not in self.usuarios:
            return f"Usuário {usuario} não encontrado."
        post = {"usuario": usuario, "mensagem": mensagem, "comentarios": []}
        self.posts.append(post)
        self.usuarios[usuario]["posts"].append(post)
        return f"Mensagem publicada por {usuario}: {mensagem}"

    def comentar_post(self, usuario, mensagem, post_index):
        if usuario not in self.usuarios:
            return f"Usuário {usuario} não encontrado."
        if post_index < 0 or post_index >= len(self.posts):
            return "Post não encontrado."
        post = self.posts[post_index]
        comentario = {"usuario": usuario, "mensagem": mensagem}
        post["comentarios"].append(comentario)
        return f"Comentário adicionado por {usuario}: {mensagem}"
    
    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            return f"Usuário {nome} encontrado."
        return f"Usuário {nome} não encontrado."
    
    def exibir_posts(self):
        if not self.posts:
            return "Não há posts disponíveis."
        resultado = []
        for i, post in enumerate(self.posts):
            comentarios = "\n".join([f"{com['usuario']}: {com['mensagem']}" for com in post["comentarios"]])
            resultado.append(f"Post {i + 1} por {post['usuario']}: {post['mensagem']}\nComentários:\n{comentarios if comentarios else 'Nenhum comentário ainda.'}")
        return "\n\n".join(resultado)


rede_social = RedeSocial()


print(rede_social.adicionar_usuario("João"))
print(rede_social.adicionar_usuario("Maria"))


print(rede_social.adicionar_amigo("João", "Maria"))


print(rede_social.publicar_mensagem("João", "Olá, pessoal!"))
print(rede_social.publicar_mensagem("Maria", "Bom dia!"))


print(rede_social.comentar_post("Maria", "Oi, João!", 0))
print(rede_social.comentar_post("João", "Oi, Maria!", 0))


print(rede_social.buscar_usuario("João"))
print(rede_social.buscar_usuario("Carlos"))


print(rede_social.exibir_posts())
