from Mae import Animal

class Cachorro(Animal):
    def __init__(self, especie, nome, cor):
        super().__init__(especie, nome)
        self._cor = cor
    
    def latir(self):
        print(f"O animal {self._especie} está latindo! (au au)")