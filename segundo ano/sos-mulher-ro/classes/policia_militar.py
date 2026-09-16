class PoliciaMilitar:
    def __init__(self, id, nome, identificacao):
        self.id = id
        self.nome = nome
        self.identificacao = identificacao
        self.viaturas = []

    def receberSolicitacao(self, ocorrencia):
        print(f"Polícia recebeu a ocorrência {ocorrencia.idOcorrencia}")

    def selecionarViatura(self):
        for viatura in self.viaturas:
            if viatura.verificarDisponibilidade():
                return viatura
        return None

    def enviarViatura(self, ocorrencia):
        viatura = self.selecionarViatura()
        if viatura:
            viatura.atualizarStatus("Em atendimento")
            return True
        return False
