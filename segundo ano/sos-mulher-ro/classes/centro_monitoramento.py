class CentroDeMonitoramento:
    def __init__(self, id, nome, status):
        self.id = id
        self.nome = nome
        self.status = status
        self.alertas = []
        self.ocorrencias = []

    def receberAlerta(self, alerta):
        self.alertas.append(alerta)

    def analisarOcorrencia(self, ocorrencia):
        print(f"Analisando ocorrência {ocorrencia.idOcorrencia}")

    def monitorarLocalizacao(self, ocorrencia):
        return ocorrencia.localizacao

    def validarOcorrencia(self, ocorrencia):
        return ocorrencia is not None

    def solicitarAtendimentoPolicial(self, ocorrencia):
        print(f"Solicitando atendimento policial: {ocorrencia.idOcorrencia}")
