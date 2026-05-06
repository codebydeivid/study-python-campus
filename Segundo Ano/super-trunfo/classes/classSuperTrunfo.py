import random

class Carta:
    #construtor
    def __init__(self, nome, resistencia, ataque, defesa, psicologico, beleza):
        self.nome = nome
        self.resistencia = resistencia
        self.ataque = ataque
        self.defesa = defesa
        self.psicologico = psicologico
        self.beleza = beleza
    
    def exibir(self):
        print("Os atributos da carta são: ")
        print(f"Resistência: {self.resistencia}\n Ataque: {self.ataque}\n Defesa: {self.defesa}\n Dano Psicológico: {self.psicologico}\n Beleza: {self.beleza}")
    
class Jogador:
    #construtor
    def __init__(self, nome, ):
        pass
        