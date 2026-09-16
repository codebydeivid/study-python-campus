from datetime import date

class MedidaProtetiva:
    def __init__(self, id, numero, dataInicio, dataFim, status):
        self.id = id
        self.numero = numero
        self.dataInicio = dataInicio
        self.dataFim = dataFim
        self.status = status

    def verificarValidade(self):
        hoje = date.today()
        return self.dataInicio <= hoje <= self.dataFim

    def verificarVigencia(self):
        return self.status.lower() == "ativa" and self.verificarValidade()
