class Alerta:
    def __init__(self, idAlerta, dataHora, status):
        self.idAlerta = idAlerta
        self.dataHora = dataHora
        self.status = status

    def enviar(self):
        return True

    def reenviar(self):
        return True

    def atualizarStatus(self, status):
        self.status = status
