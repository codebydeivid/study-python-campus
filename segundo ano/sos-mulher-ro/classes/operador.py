from .usuario import Usuario

class Operador(Usuario):
    def __init__(self, id, nome, email, telefone, senha, status, cargo, matricula):
        super().__init__(id, nome, email, telefone, senha, status)
        self.cargo = cargo
        self.matricula = matricula

    def analisarOcorrencia(self, ocorrencia):
        print(f"Analisando ocorrência {ocorrencia.idOcorrencia}")

    def consultarOcorrencia(self, id):
        return None
