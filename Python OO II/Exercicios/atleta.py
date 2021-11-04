class Atleta:

    def __init__(self, aposentado, peso): #Método constutor
        self.aposentado = aposentado
        self.peso = peso
    
    def aposentar(self):
        pass
    
    def aquecer(self):
        pass

class Corredor(Atleta):

    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def correr(self):
        print("Correndo...")

class Nadador(Atleta):

    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def nadar(self):
        print("Nadando...")

class Ciclista(Atleta):

    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

    def pedalar(self):
        print("Pedalando...")

class TriAtleta(Corredor, Nadador, Ciclista):
    
    def __init__(self, aposentado, peso):
        super().__init__(aposentado, peso)

vinicius = TriAtleta("Não", 80)

print(vinicius.correr())

print(vinicius.nadar())

print(vinicius.pedalar())