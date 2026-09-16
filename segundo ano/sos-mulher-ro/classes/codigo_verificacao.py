from datetime import datetime

class CodigoDeVerificacao:
    def __init__(self, id, codigo, tipoEnvio, dataGeracao, dataExpiracao, utilizado):
        self.id = id
        self.codigo = codigo
        self.tipoEnvio = tipoEnvio
        self.dataGeracao = dataGeracao
        self.dataExpiracao = dataExpiracao
        self.utilizado = utilizado

    def validar(self, codigoInformado):
        if self.verificarExpiracao():
            return False
        if self.codigo == codigoInformado and not self.utilizado:
            self.utilizado = True
            return True
        return False

    def verificarExpiracao(self):
        return datetime.now() > self.dataExpiracao

    def reenviar(self):
        self.utilizado = False
        self.dataGeracao = datetime.now()
