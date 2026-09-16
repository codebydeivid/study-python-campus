class Viatura:
    def __init__(self, id, identificacao, status, localizacaoAtual):
        self.id = id
        self.identificacao = identificacao
        self.status = status
        self.localizacaoAtual = localizacaoAtual
        self.atendimentos = []

    def verificarDisponibilidade(self):
        return self.status.lower() == "disponível"

    def atualizarStatus(self, status):
        self.status = status

    def atualizarLocalizacao(self, localizacao):
        self.localizacaoAtual = localizacao
