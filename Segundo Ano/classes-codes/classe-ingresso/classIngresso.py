class Ingresso:
    #construtor
    def __init__(self, valor:int):
        #atributos
        self.valor = valor
    
    def exibir(self):
        print(f"O valor do ingresso é R${self.valor}.")

class IngressoVIP(Ingresso):
    #construtor
    def __init__(self, valor:int, adicional:int):
        super().__init__(valor)
        self.adicional = adicional

    def valorAdicional(self):
        return self.valor + self.adicional
    
    def exibir(self):
        print("-"*10)
        super().exibir()
        print(f"O adicional é R${self.adicional} ficando com o total de R${self.valorAdicional()}")
        print("-"*10)