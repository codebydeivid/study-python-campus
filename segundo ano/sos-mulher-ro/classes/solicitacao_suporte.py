class SolicitacaoDeSuporte:
    def __init__(self, id, tipo, dataHora, status):
        self.id = id
        self.tipo = tipo
        self.dataHora = dataHora
        self.status = status
        self.atendimento = None

    def registrar(self):
        print(f"Solicitação {self.id} registrada.")

    def encaminharParaEquipe(self):
        print(f"Solicitação {self.id} encaminhada.")

    def atualizarStatus(self, status):
        self.status = status
