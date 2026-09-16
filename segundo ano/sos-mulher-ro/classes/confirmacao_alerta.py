from datetime import datetime

class ConfirmacaoDeAlerta:
    def __init__(self, id, mensagem, dataHoraEnvio, statusEnvio):
        self.id = id
        self.mensagem = mensagem
        self.dataHoraEnvio = dataHoraEnvio
        self.statusEnvio = statusEnvio

    def gerarMensagem(self):
        return self.mensagem

    def enviar(self):
        self.dataHoraEnvio = datetime.now()
        self.statusEnvio = "Enviado"
        return True

    def reenviar(self):
        self.dataHoraEnvio = datetime.now()
        self.statusEnvio = "Reenviado"
        return True
