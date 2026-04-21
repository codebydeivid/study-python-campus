class Aquecedor:
    def __init__(self):
        self.temperatura = 15.0

    def aquecer(self, temperatura):
        temperatura+=5
        return self.temperatura

    def esfriar(self, temperatura):
        temperatura-=5
        return self.temperatura

    def getTemperatura(self):
        return self.temperatura                             
    
