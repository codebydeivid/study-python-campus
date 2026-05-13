import random
from classes.classSuperTrunfo import *

#Variáveis
nome = input("Qual o seu nome? ")
um_mano = Jogador("Você", eh_cpu=False)
cpu = Jogador("CPU", eh_cpu=True)

baralho = Jogo.criar_baralho()
random.shuffle(baralho)

metade = len(baralho) // 2
um_mano.distribuir_cartas(baralho[:metade])
cpu.distribuir_cartas(baralho[metade:])

Jogo.cabecalho("SUPER TRUNFO - BATALHA DE ARTRÓPODES")

print(f"\n  Cartas distribuídas: {um_mano.get_nome()} e {cpu.get_nome()} receberam {metade} cartas cada.\n")

rodada = 0

while not um_mano.esta_sem_cartas() and not cpu.esta_sem_cartas():
    rodada += 1
    Jogo.cabecalho(
        f"RODADA {rodada}  |  "
        f"{um_mano.get_nome()}: {um_mano.get_quantidade_cartas()} carta(s)  |  "
        f"{cpu.get_nome()}: {cpu.get_quantidade_cartas()} carta(s)"
    )

    print(f"\n  [ Sua vez {nome} ]")
    carta_h, idx_h = um_mano.escolher_carta()
    indice_atrib   = um_mano.escolher_atributo()
    nome_atrib     = Carta.ATRIBUTOS[indice_atrib]

    carta_cpu, idx_cpu = cpu.escolher_carta()

    Jogo.cabecalho(f"DISPUTA: {nome_atrib.upper()}")

    print(f"\n  CARTA DE {um_mano.get_nome().upper()}:")
    carta_h.exibir_carta()

    print(f"\n  CARTA DA {cpu.get_nome()}:")
    carta_cpu.exibir_carta()

    valor_h   = carta_h.get_atributo_por_indice(indice_atrib)
    valor_cpu = carta_cpu.get_atributo_por_indice(indice_atrib)

    print(f"\n  {carta_h.get_nome():<28} -> {nome_atrib}: {valor_h}")
    print(f"  {carta_cpu.get_nome():<28} -> {nome_atrib}: {valor_cpu}")

    resultado = Jogador.comparar_cartas(carta_h, carta_cpu, indice_atrib)

    if resultado == 1:
        print(f"\n  {um_mano.get_nome()} VENCEU esta rodada! (+1 carta)")
        um_mano.transferir_carta(cpu, idx_cpu)

    elif resultado == -1:
        print(f"\n  {cpu.get_nome()} VENCEU esta rodada! (-1 carta)")
        cpu.transferir_carta(um_mano, idx_h)

    else:
        print(f"\n  EMPATE! Cada um fica com sua carta.")

    Jogo.pausar()

Jogo.cabecalho("FIM DE JOGO")
print(f"\n  Rodadas disputadas:{rodada}")
print(f"  Vitórias de {um_mano.get_nome():<12}: {um_mano.get_vitorias()}")
print(f"  Vitórias da {cpu.get_nome():<12}: {cpu.get_vitorias()}")

if cpu.esta_sem_cartas():
    print(f"\n PARABÉNS! Você conquistou todas as cartas e GANHOU!")
elif um_mano.esta_sem_cartas():
    print(f"\n A CPU ficou com todas as cartas. Você PERDEU!")
else:
    print(f"\n A partida terminou em EMPATE!")