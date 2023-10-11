class Animal:
    def __init__(self, especie, nome):
        self._especie = especie
        self._nome = nome
    
    def comunicar(self):
        print(f"O animal {self._especie} fez um barulho!")
    
    def movimentar(self):
        print(f"O animal {self._especie} está se movimentando!")