class Imovel:
    def __init__(self, endereco, preco):
        self.__endereco = endereco
        self.__preco = preco
    
    def __getattr__(self):
        return self.__endereco, self.__preco
    
    def __setattr__(self, name, value):
        pass