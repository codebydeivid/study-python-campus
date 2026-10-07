class Pilha:
    def __init__(self):
        self.dados = []

    def empilhar(self, item):
        self.dados.append(item)

    def desempilhar(self):
        self.dados.pop(-1)