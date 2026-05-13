import random
from classes.classSuperTrunfo import *

def criar_baralho() -> list[Carta]:
    return [
        Carta("Formiga de Mel",      10,  10, 15,   5,  95),
        Carta("Barata",              80,  30, 90,  90,  10),
        Carta("Abelha",              30,  40, 40,  50,  80),
        Carta("Escorpião",          100,  85, 65,  90,  40),
        Carta("Mariposa",            50,  20, 30,  60, 100),
        Carta("Louva-Deus",          70,  40, 45,  30, 100),
        Carta("Lacraia",             95,  90, 40, 100,  50),
        Carta("Aranha Viúva Negra", 100,  90, 50, 100,  90),
    ]

def cabecalho(texto: str) -> None:
    print("\n" + "=" * 46)
    print(f"  {texto}")
    print("=" * 46)


def pausar() -> None:
    input("\n Pressione ENTER para continuar.")

def jogar() -> None:
    cabecalho("SUPER TRUNFO - BATALHA DE ARTRÓPODES")

    humano = Jogador("Você",  eh_cpu=False)
    cpu    = Jogador("CPU",   eh_cpu=True)

    baralho = criar_baralho()
    random.shuffle(baralho)

    metade = len(baralho) // 2
    humano.distribuir_cartas(baralho[:metade])
    cpu.distribuir_cartas(baralho[metade:])

    print(f"\n  Cartas distribuídas: {humano.get_nome()} e {cpu.get_nome()} receberam {metade} cartas cada.\n")

    rodada = 0

    while not humano.esta_sem_cartas() and not cpu.esta_sem_cartas():
        rodada += 1
        cabecalho(
            f"RODADA {rodada}  |  "
            f"{humano.get_nome()}: {humano.get_quantidade_cartas()} carta(s)  |  "
            f"{cpu.get_nome()}: {cpu.get_quantidade_cartas()} carta(s)"
        )

        print(f"\n  [ Vez de {humano.get_nome()} ]")
        carta_h, idx_h = humano.escolher_carta()
        indice_atrib   = humano.escolher_atributo()
        nome_atrib     = Carta.ATRIBUTOS[indice_atrib]

        carta_cpu, idx_cpu = cpu.escolher_carta()

        cabecalho(f"DISPUTA: {nome_atrib.upper()}")

        print(f"\n  CARTA DE {humano.get_nome().upper()}:")
        carta_h.exibir_carta()

        print(f"\n  CARTA DA {cpu.get_nome()}:")
        carta_cpu.exibir_carta()

        # --- Valores disputados ---
        valor_h   = carta_h.get_atributo_por_indice(indice_atrib)
        valor_cpu = carta_cpu.get_atributo_por_indice(indice_atrib)

        print(f"\n  {carta_h.get_nome():<28} → {nome_atrib}: {valor_h}")
        print(f"  {carta_cpu.get_nome():<28} → {nome_atrib}: {valor_cpu}")

        resultado = Jogador.comparar_cartas(carta_h, carta_cpu, indice_atrib)

        if resultado == 1:
            print(f"\n  {humano.get_nome()} VENCEU esta rodada! (+1 carta)")
            humano.transferir_carta(cpu, idx_cpu)

        elif resultado == -1:
            print(f"\n  {cpu.get_nome()} VENCEU esta rodada! (-1 carta)")
            cpu.transferir_carta(humano, idx_h)

        else:
            print(f"\n  EMPATE! Cada um fica com sua carta.")

        pausar()

    cabecalho("FIM DE JOGO")
    print(f"\n  Rodadas disputadas      : {rodada}")
    print(f"  Vitórias de {humano.get_nome():<12}: {humano.get_vitorias()}")
    print(f"  Vitórias da {cpu.get_nome():<12}: {cpu.get_vitorias()}")

    if cpu.esta_sem_cartas():
        print(f"\n PARABÉNS! Você conquistou todas as cartas e GANHOU!")
    elif humano.esta_sem_cartas():
        print(f"\n A CPU ficou com todas as cartas. Você PERDEU!")
    else:
        print(f"\n A partida terminou em EMPATE!")

    print()

if __name__ == "__main__":
    jogar()