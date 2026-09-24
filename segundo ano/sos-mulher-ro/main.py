from datetime import datetime, date

from classes.vitima import Vitima
from classes.agressor import Agressor
from classes.tornozeleira_eletronica import TornozeleiraEletronica
from classes.medida_protetiva import MedidaProtetiva
from classes.ocorrencia import Ocorrencia
from classes.localizacao import Localizacao
from classes.alerta import Alerta
from classes.confirmacao_alerta import ConfirmacaoDeAlerta
from classes.centro_monitoramento import CentroDeMonitoramento
from classes.policia_militar import PoliciaMilitar
from classes.viatura import Viatura
from classes.atendimento_policial import AtendimentoPolicial
from classes.equipe_apoio import EquipeDeApoio

vitimas = []
ocorrencias = []
contador_ocorrencia = 1
contador_alerta = 1
contador_atendimento_policial = 1


def linha():
    print("-" * 62)

# Cadastro da vitima
def cadastrar_vitima():
    linha()
    print("CADASTRO DE VÍTIMA")
    nome = input("Nome: ").strip() or "Sem nome"
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()
    senha = input("Senha: ").strip()
    cpf = input("CPF: ").strip()

    nascimento_str = input("Data de nascimento (AAAA-MM-DD): ").strip()
    try:
        ano, mes, dia = map(int, nascimento_str.split("-"))
        nascimento = date(ano, mes, dia)
    except (ValueError, AttributeError):
        print("Data inválida.")
        nascimento = date(2000, 1, 1)

    possui_medida = input("Possui medida protetiva válida? (s/n): ").strip().lower() == "s"

    vitima = Vitima(
        id=len(vitimas) + 1,
        nome=nome,
        email=email,
        telefone=telefone,
        senha=senha,
        status="Ativa",
        cpf=cpf,
        dataNascimento=nascimento,
        medidaProtetivaValida=possui_medida,
    )

    # efetuarCadastro() é o método da classe Vitima que representa a confirmação do cadastro, retorna um bolleano.
    if vitima.efetuarCadastro():
        vitimas.append(vitima)

    if possui_medida:
        medida = MedidaProtetiva(
            id=len(vitima.medidasProtetivas) + 1,
            numero=f"MP-{vitima.id:04d}",
            dataInicio=date(2026, 1, 1),
            dataFim=date(2027, 1, 1),
            status="Ativa",
        )
        vitima.medidasProtetivas.append(medida)

    print(f"\nVítima '{vitima.nome}' cadastrada com sucesso!")
    return vitima

# Associações das classes do diagrama
def acionar_alerta(vitima, centro, policia):
    global contador_ocorrencia, contador_alerta, contador_atendimento_policial

    linha()
    print(f"{vitima.nome} está acionando o botão de emergência!")
    vitima.solicitarAjuda()

    descricao = input("Oque está acontecendo? ").strip() or "Situação de risco"
    lat_str = input("Latitude atual: ").strip() or "-8.7619"
    lon_str = input("Longitude atual: ").strip() or "-63.9039"
    endereco = input("Endereço aproximado: ").strip() or "Endereço não informado"

    try:
        lat, lon = float(lat_str), float(lon_str)
    except ValueError:
        print("Coordenadas inválidas.")

    # Localizacao é criada e associada à Ocorrencia
    localizacao = Localizacao(lat, lon, endereco, datetime.now())

    # A Ocorrencia é registrada e vinculada à Vitima
    ocorrencia = Ocorrencia(
        idOcorrencia=f"OC{contador_ocorrencia:03d}",
        dataHora=datetime.now(),
        status="Aberta",
        descricao=descricao,
    )
    contador_ocorrencia += 1
    ocorrencia.vitima = vitima
    ocorrencia.adicionarLocalizacao(localizacao)
    vitima.ocorrencias.append(ocorrencia)
    ocorrencia.registrar()

    # Um alerta é gerado a partir da Ocorrencia e enviado
    alerta = Alerta(idAlerta=f"AL{contador_alerta:03d}", dataHora=datetime.now(), status="Pendente")
    contador_alerta += 1
    ocorrencia.alertas.append(alerta)

    print(f"\nEnviando alerta {alerta.idAlerta}.")
    if alerta.enviar():
        alerta.atualizarStatus("Enviado")
        print("Alerta enviado com sucesso ao Centro de Monitoramento.")

    # O CentroDeMonitoramento recebe o alerta e a ocorrência
    centro.receberAlerta(alerta)
    ocorrencia.encaminharParaMonitoramento()

    if not centro.validarOcorrencia(ocorrencia):
        print("Não foi possível validar a ocorrência.")
        ocorrencias.append(ocorrencia)
        return

    print("Ocorrência validada pelo Centro de Monitoramento.")
    centro.analisarOcorrencia(ocorrencia)
    localizacao_monitorada = centro.monitorarLocalizacao(ocorrencia)
    print(f"Localização monitorada em tempo real: {localizacao_monitorada.obterCoordenadas()}")

    # O Centro aciona a PoliciaMilitar, que tenta despachar uma Viatura
    centro.solicitarAtendimentoPolicial(ocorrencia)
    policia.receberSolicitacao(ocorrencia)

    if policia.enviarViatura(ocorrencia):
        print("Viatura despachada e a caminho do local.")

        # Abre-se um AtendimentoPolicial para acompanhar o caso
        atendimento = AtendimentoPolicial(
            id=contador_atendimento_policial,
            dataHoraAcionamento=None,
            dataHoraChegada=None,
            status="Pendente",
        )
        contador_atendimento_policial += 1
        atendimento.registrarAcionamento()
        atendimento.iniciarAtendimento()
        print(f"Atendimento policial {atendimento.id} iniciado - status: {atendimento.status}")
    else:
        print("Nenhuma viatura disponível no momento!")

    # Uma ConfirmacaoDeAlerta é enviada de volta para a vítima
    confirmacao = ConfirmacaoDeAlerta(
        id=alerta.idAlerta,
        mensagem=f"Ajuda a caminho para {vitima.nome}. Mantenha-se em local seguro.",
        dataHoraEnvio=None,
        statusEnvio="Pendente",
    )
    confirmacao.enviar()
    print(f'\nConfirmação enviada para {vitima.nome}: "{confirmacao.gerarMensagem()}"')

    ocorrencias.append(ocorrencia)


# Suportes
def solicitar_suporte(vitima, equipes):
    linha()
    print("Tipos de suporte disponíveis: psicológico, jurídico")
    tipo = input("Qual tipo de suporte deseja solicitar? ").strip()

    # A própria Vitima cria a SolicitacaoDeSuporte
    solicitacao = vitima.solicitarSuporte(tipo)
    solicitacao.registrar()

    equipe_disponivel = next((e for e in equipes if e.verificarDisponibilidade()), None)

    if not equipe_disponivel:
        print("Nenhuma equipe de apoio disponível no momento.")
        return

    equipe_disponivel.receberSolicitacao(solicitacao)
    atendimento = equipe_disponivel.definirSuporte(tipo)
    solicitacao.atendimento = atendimento
    solicitacao.encaminharParaEquipe()
    equipe_disponivel.encaminharSuporte()
    atendimento.iniciarAtendimento()

    print(
        f"\nEquipe de apoio,\nespecialidade={equipe_disponivel.especialidade}) está atendendo.\nStatus do atendimento: {atendimento.status}"
    )


# Consultas auxiliares
def verificar_medida_protetiva(vitima):
    linha()
    if not vitima.medidasProtetivas:
        print(f"{vitima.nome} não possui medida protetiva cadastrada.")
        return
    for medida in vitima.medidasProtetivas:
        vigente = medida.verificarVigencia()
        print(f"Medida {medida.numero}: {'VIGENTE' if vigente else 'NÃO VIGENTE'}")


def verificar_tornozeleira(agressor):
    linha()
    if not agressor.possuiTornozeleira():
        print(f"{agressor.nome} não possui tornozeleira eletrônica cadastrada.")
        return
    tornozeleira = agressor.tornozeleira
    print(f"Tornozeleira {tornozeleira.idDispositivo} - status: {tornozeleira.status}")
    print(f"Está ativa? {'Sim' if tornozeleira.estaAtiva() else 'Não'}")
    print(f"Sinal sendo transmitido? {'Sim' if tornozeleira.enviarSinal() else 'Não'}")
    localizacao = tornozeleira.obterLocalizacao()
    print(f"Última localização conhecida: {localizacao.obterCoordenadas()} ({localizacao.endereco})")

def ambiente_simulado():
    viatura1 = Viatura(1, "VTR-101", "Disponível", Localizacao(-8.67, -69.96, "Base Central", datetime.now()))
    viatura2 = Viatura(2, "VTR-102", "Disponível", Localizacao(-8.24, -70.90, "Base Norte", datetime.now()))

    policia = PoliciaMilitar(1, "1º BPM - Porto Velho", "PM-RO-001")
    policia.viaturas = [viatura1, viatura2]

    centro = CentroDeMonitoramento(1, "Central de Monitoramento RO", "Ativo")

    equipes = [
        EquipeDeApoio(1, "Psicológico", True, "Remoto"),
        EquipeDeApoio(2, "Jurídico", True, "Presencial"),
    ]

    agressor = Agressor(1, "Agressor Cadastrado", "000.000.000-00")
    agressor.tornozeleira = TornozeleiraEletronica(
        idDispositivo="TZ-001",
        status="Ativa",
        dataAtivacao=date(2026, 1, 1),
        ultimaLocalizacao=Localizacao(-8.75, -63.90, "Zona Sul", datetime.now()),
    )

    return policia, centro, equipes, agressor

# Menu principal
def menu():
    policia, centro, equipes, agressor = ambiente_simulado()
    vitima_logada = None

    opcoes = {
        "1": "Cadastrar vítima",
        "2": "Acionar alerta de emergência (botão do pânico)",
        "3": "Solicitar suporte (psicológico/jurídico)",
        "4": "Verificar medida protetiva da vítima ativa",
        "5": "Verificar tornozeleira eletrônica do agressor",
        "0": "Sair",
    }

    linha()
    print(" SISTEMA DE PROTEÇÃO À VÍTIMA - TESTE")
    linha()

    while True:
        for chave, texto in opcoes.items():
            print(f"{chave} - {texto}")

        escolha = input("\nEscolha uma opção: ").strip()

        if escolha == "1":
            vitima_logada = cadastrar_vitima()
        elif escolha == "2":
            if vitima_logada:
                acionar_alerta(vitima_logada, centro, policia)
            else:
                print("Cadastre uma vítima primeiro.")
        elif escolha == "3":
            if vitima_logada:
                solicitar_suporte(vitima_logada, equipes)
            else:
                print("Cadastre uma vítima primeiro.")
        elif escolha == "4":
            if vitima_logada:
                verificar_medida_protetiva(vitima_logada)
            else:
                print("Cadastre uma vítima primeiro.")
        elif escolha == "5":
            verificar_tornozeleira(agressor)
        elif escolha == "0":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
