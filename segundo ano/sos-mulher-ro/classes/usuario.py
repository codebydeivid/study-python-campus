class Usuario:
    def __init__(self, id, nome, email, telefone, senha, status):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.status = status

    def autenticar(self, email, senha):
        return self.email == email and self.senha == senha

    def alterarSenha(self, novaSenha):
        self.senha = novaSenha

    def recuperarAcesso(self):
        print(f"Acesso recuperado para {self.email}")
