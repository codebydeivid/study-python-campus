class MaquinaDeIngressos:
    # construtor <- essa é a base de todos os objetos que serão criados depois
    def __init__(self, preco):
        self.preco=preco
        self.saldo=0
        self.total=0
    
    # métodos
    def getPreco(self):
        return self.preco

    def definirPreco(self, novoPreco):
        self.preco=novoPreco

    def imprimirIngresso(self):
        if self.saldo >= self.preco:
            print("#" * 20)
            print("#     Ingresso     #")
            print(f"#   Preço: R$ {self.preco}   #")
            print("#" * 20)
            self.total += self.saldo
            self.saldo -= self.preco
        else:
            print("Saldo insuficiente")

    def descontoPreco(self, valor):
        self.preco -= valor
    
    def inserirDinheiro(self, novoSaldo):
        if novoSaldo >= 0:
            self.saldo += novoSaldo
        else:
            print("Tá errado!")
