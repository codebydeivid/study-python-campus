class AtendimentoDeSuporte:
    def __init__(self, id, tipo, descricao, dataHora, status):
        self.id = id
        self.tipo = tipo
        self.descricao = descricao
        self.dataHora = dataHora
        self.status = status

    def iniciarAtendimento(self):
        self.status = "Em atendimento"

    def registrarAtendimento(self):
        print(f"Atendimento {self.id} registrado.")

    def finalizarAtendimento(self):
        self.status = "Finalizado"

    def atualizarStatus(self, status):
        self.status = status
