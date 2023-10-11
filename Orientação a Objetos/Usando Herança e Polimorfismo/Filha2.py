from Mae import Animal

class Golfinho(Animal):
    def __init__(self, especie, nome, cor):
        super().__init__(especie, nome)
        self._cor = cor
        
    def nadar(self):
        print(f"O animal {self._especie} {self._nome} está nadando!")
        
    