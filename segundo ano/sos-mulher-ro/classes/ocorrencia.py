class Ocorrencia:
    def __init__(self, idOcorrencia, dataHora, status, descricao):
        self.idOcorrencia = idOcorrencia
        self.dataHora = dataHora
        self.status = status
        self.descricao = descricao
        self.localizacao = None
        self.vitima = None
        self.alertas = []

    def registrar(self):
        print(f"Ocorrência {self.idOcorrencia} registrada.")

    def adicionarLocalizacao(self, localizacao):
        self.localizacao = localizacao

    def atualizarStatus(self, status):
        self.status = status

    def encaminharParaMonitoramento(self):
        print(f"Ocorrência {self.idOcorrencia} encaminhada para monitoramento.")
