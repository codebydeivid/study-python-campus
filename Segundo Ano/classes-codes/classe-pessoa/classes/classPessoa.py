#criar a classe pessoa
class Pessoa:
    #construtor
    def __init__(self, nome, sobrenome, genero, idade, altura, peso, oMedoAbundanteDeTodasAsVerdades):
        self.nome = nome
        self.sobrenome = sobrenome
        self.genero = genero
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.oMedoAbundanteDeTodasAsVerdades = oMedoAbundanteDeTodasAsVerdades
    
    def exibir(self):
        print("-" * 30)
        print(f"Olá {self.nome} {self.sobrenome}, muito prazer!")
        print("-" * 30)
        print(f"Você é {self.genero}\n Tem {self.idade} anos\n Tem {self.altura}m de altura\n E pesa {self.peso} kg.")
        print("-" * 30)
        print(f"O preço do medo abundante de todas as verdades é {self.oMedoAbundanteDeTodasAsVerdades}.")

class Empregado(Pessoa):
    #construtor
    def __init__(self, matricula, salario, nome, sobrenome, genero, idade, altura, peso, oMedoAbundanteDeTodasAsVerdades):
        self.matricula=matricula
        self.salario=salario
        super().__init__(nome, sobrenome, genero, idade, altura, peso, oMedoAbundanteDeTodasAsVerdades)
    
    def exibir(self):
        super().exibir()
        print("-" * 30)
        print(f"Sua matricula é {self.matricula} e seu salario é {self.salario}.")
        print("-" * 30)

class Chefe(Empregado):
    #contrutor
    def __init__(self, matricula, salario, nome, sobrenome, genero, idade, altura, peso, oMedoAbundanteDeTodasAsVerdades, bonus):
        #atributos
        self.bonus = bonus
        super().__init__(matricula, salario, nome, sobrenome, genero, idade, altura, peso, oMedoAbundanteDeTodasAsVerdades)
    
    def CalcularBonus(self):
        return int(self.salario) + int(self.bonus)
    
    def exibir(self):
        super().exibir()
        print(f"Como vc é chefe você tem um bonus de {self.bonus} tendo um salário total de {self.CalcularBonus()}")
        print("-" * 30)
    
