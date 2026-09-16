from .atendimento_suporte import AtendimentoDeSuporte
from datetime import datetime

class EquipeDeApoio:
    def __init__(self, id, especialidade, disponibilidade, tipoAtendimento):
        self.id = id
        self.especialidade = especialidade
        self.disponibilidade = disponibilidade
        self.tipoAtendimento = tipoAtendimento

    def receberSolicitacao(self, solicitacao):
        print(f"Equipe {self.id} recebeu a solicitação {solicitacao.id}")

    def verificarDisponibilidade(self):
        return self.disponibilidade

    def definirSuporte(self, tipo):
        return AtendimentoDeSuporte(
            1, tipo, "Atendimento solicitado", datetime.now(), "Pendente"
        )

    def encaminharSuporte(self):
        print(f"Equipe {self.id} encaminhando suporte.")
