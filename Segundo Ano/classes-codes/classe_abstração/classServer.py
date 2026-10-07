from abc import ABC 

class Servidor(ABC):
    @abstractmethod
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

