from datetime import datetime

class Localizacao:
    def __init__(self, latitude, longitude, endereco, timestamp):
        self.latitude = latitude
        self.longitude = longitude
        self.endereco = endereco
        self.timestamp = timestamp

    def obterCoordenadas(self):
        return f"{self.latitude}, {self.longitude}"

    def atualizar(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = datetime.now()
