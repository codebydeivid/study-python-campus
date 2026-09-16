class Agressor:
    def __init__(self, id, nome, cpf):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.tornozeleira = None

    def possuiTornozeleira(self):
        return self.tornozeleira is not None
