from datetime import datetime

class AtendimentoPolicial:
    def __init__(self, id, dataHoraAcionamento, dataHoraChegada, status):
        self.id = id
        self.dataHoraAcionamento = dataHoraAcionamento
        self.dataHoraChegada = dataHoraChegada
        self.status = status

    def iniciarAtendimento(self):
        self.status = "Em atendimento"

    def registrarAcionamento(self):
        self.dataHoraAcionamento = datetime.now()

    def finalizarAtendimento(self):
        self.status = "Finalizado"

    def atualizarStatus(self, status):
        self.status = status
