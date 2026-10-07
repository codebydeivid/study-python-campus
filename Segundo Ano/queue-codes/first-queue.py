class Fila:
    def __init__(self):
        self.dados=[]

    def inserir(self, item):
        self.dados.append(item)

    def remover(self):
        self.dados.pop(0)