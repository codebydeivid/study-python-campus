from datetime import datetime, date
from classes.vitima import Vitima
from classes.ocorrencia import Ocorrencia
from classes.localizacao import Localizacao

def main():
    localizacao = Localizacao(
        -8.7619, -63.9039, "Porto Velho - RO", datetime.now()
    )

    vitima = Vitima(
        1, "Maria", "maria@email.com", 999999999,
        "1234", "Ativa", 123456789, date(2005, 5, 10), True
    )

    ocorrencia = Ocorrencia(
        "OC001", datetime.now(), "Aberta",
        "Ocorrência registrada pela vítima."
    )

    ocorrencia.vitima = vitima
    ocorrencia.adicionarLocalizacao(localizacao)
    vitima.ocorrencias.append(ocorrencia)

    ocorrencia.registrar()
    ocorrencia.encaminharParaMonitoramento()
    print("Coordenadas:", ocorrencia.localizacao.obterCoordenadas())

if __name__ == "__main__":
    main()  
