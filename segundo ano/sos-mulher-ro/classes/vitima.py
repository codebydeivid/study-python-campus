from .usuario import Usuario
from .solicitacao_suporte import SolicitacaoDeSuporte
from datetime import datetime

class Vitima(Usuario):
    def __init__(self, id, nome, email, telefone, senha, status, cpf, dataNascimento, medidaProtetivaValida):
        super().__init__(id, nome, email, telefone, senha, status)
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.medidaProtetivaValida = medidaProtetivaValida
        self.codigosVerificacao = []
        self.ocorrencias = []
        self.medidasProtetivas = []
        self.solicitacoesSuporte = []

    def efetuarCadastro(self):
        return True

    def solicitarAjuda(self):
        print(f"{self.nome} solicitou ajuda.")

    def solicitarSuporte(self, tipo):
        solicitacao = SolicitacaoDeSuporte(
            len(self.solicitacoesSuporte) + 1, tipo, datetime.now(), "Pendente"
        )
        self.solicitacoesSuporte.append(solicitacao)
        return solicitacao

    def informarLocalizacao(self):
        return self.ocorrencias[-1].localizacao if self.ocorrencias else None
