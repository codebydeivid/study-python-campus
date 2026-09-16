class TornozeleiraEletronica:
    def __init__(self, idDispositivo, status, dataAtivacao, ultimaLocalizacao):
        self.idDispositivo = idDispositivo
        self.status = status
        self.dataAtivacao = dataAtivacao
        self.ultimaLocalizacao = ultimaLocalizacao

    def obterLocalizacao(self):
        return self.ultimaLocalizacao

    def enviarSinal(self):
        return self.status.lower() == "ativa"

    def estaAtiva(self):
        return self.status.lower() == "ativa"
