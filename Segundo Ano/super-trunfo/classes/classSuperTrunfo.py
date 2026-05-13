import os
import random

class Carta:
    ATRIBUTOS = {
        1: "Resistência HP",
        2: "Ataque",
        3: "Defesa",
        4: "Dano Psicológico",
        5: "Beleza",
    }

    def __init__(self, nome: str, resistencia_hp: int, ataque: int, defesa: int, dano_psicologico: int, beleza: int):
        self.__nome = nome
        self.__resistencia_hp = resistencia_hp
        self.__ataque = ataque
        self.__defesa = defesa
        self.__dano_psicologico = dano_psicologico
        self.__beleza = beleza

    def get_nome(self):
        return self.__nome

    def get_resistencia_hp(self):
        return self.__resistencia_hp

    def get_ataque(self):
        return self.__ataque

    def get_defesa(self):
        return self.__defesa

    def get_dano_psicologico(self):
        return self.__dano_psicologico

    def get_beleza(self):
        return self.__beleza
    
    def get_atributo_por_indice(self, indice: int):
        mapa = {
            1: self.__resistencia_hp,
            2: self.__ataque,
            3: self.__defesa,
            4: self.__dano_psicologico,
            5: self.__beleza,
        }

        return mapa[indice]
    
    def exibir_carta(self):
        print(f"{self.__nome}")
        print(f"{'1 - Resistência HP':<22} {self.__resistencia_hp:>5} pts")
        print(f"{'2 - Ataque':<22} {self.__ataque:>5} pts")
        print(f"{'3 - Defesa':<22} {self.__defesa:>5} pts")
        print(f"{'4 - Dano Psicológico':<22} {self.__dano_psicologico:>5} pts")
        print(f"{'5 - Beleza':<22} {self.__beleza:>5} pts")

    def __str__(self):
        return (
            f"Carta({self.__nome} | "
            f"HP:{self.__resistencia_hp} Ataque:{self.__ataque} "
            f"Defesa:{self.__defesa} Psicologo:{self.__dano_psicologico} "
            f"Buniteza:{self.__beleza})"
        )
class Jogador:
    def __init__(self, nome: str, eh_cpu: bool = False):
        self.__nome     = nome
        self.__mao      = []
        self.__eh_cpu   = eh_cpu
        self.__vitorias = 0

    def get_nome(self):
        return self.__nome

    def get_mao(self):
        return self.__mao

    def get_quantidade_cartas(self):
        return len(self.__mao)

    def get_vitorias(self):
        return self.__vitorias

    def eh_cpu(self):
        return self.__eh_cpu

    def esta_sem_cartas(self):
        return len(self.__mao) == 0

    def set_nome(self, nome: str):
        self.__nome = nome

    def _incrementar_vitorias(self):
        self.__vitorias += 1

    def distribuir_cartas(self, cartas: list[Carta]):
        self.__mao = list(cartas)

    def exibir_mao(self):
        print(f"\n  Cartas de {self.__nome}:")
        for i, carta in enumerate(self.__mao, start=1):
            print(f"\n  === Carta {i} ===")
            carta.exibir_carta()

    def escolher_carta(self):
        if self.__eh_cpu:
            idx = random.randint(0, len(self.__mao) - 1)
            return self.__mao[idx], idx

        self.exibir_mao()
        while True:
            try:
                escolha = int(input(f"\n  Qual carta você quer jogar? (1-{len(self.__mao)}): "))
                if 1 <= escolha <= len(self.__mao):
                    idx = escolha - 1
                    return self.__mao[idx], idx
                print(f"Digite um número entre 1 e {len(self.__mao)}.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    def escolher_atributo(self):
        if self.__eh_cpu:
            return random.randint(1, 5)

        print("\nEscolha o atributo para disputar:")
        for idx, nome in Carta.ATRIBUTOS.items():
            print(f"    [{idx}] {nome}")

        while True:
            try:
                escolha = int(input("\nSua escolha (1-5): "))
                if 1 <= escolha <= 5:
                    return escolha
                print("Digite um número entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    def comparar_cartas(carta_a: Carta, carta_b: Carta, indice_atributo: int):
        valor_a = carta_a.get_atributo_por_indice(indice_atributo)
        valor_b = carta_b.get_atributo_por_indice(indice_atributo)

        if valor_a > valor_b:
            return 1
        if valor_b > valor_a:
            return -1
        return 0

    def transferir_carta(self, adversario: "Jogador", idx_carta_adversario: int) -> None:
        carta_ganha = adversario._remover_carta(idx_carta_adversario)
        self.__mao.append(carta_ganha)
        self._incrementar_vitorias()

    def _remover_carta(self, indice: int) -> Carta:
        return self.__mao.pop(indice)

    def __str__(self) -> str:
        return (
            f"Jogador({self.__nome}"
            f"Cartas: {len(self.__mao)}"
            f"Vitórias: {self.__vitorias})"
        )

class Jogo:
    def criar_baralho():
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

    def cabecalho(texto: str):
        print("\n" + "=" * 46)
        print(f"  {texto}")
        print("=" * 46)

    def pausar():
        input("\n Pressione ENTER para continuar.")
        os.system("cls")