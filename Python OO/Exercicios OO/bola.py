
class Bola:

    def __init__(self, cor, circuferencia, material): #Método construtor
        self.__cor = cor
        self.__circuferencia = circuferencia
        self.__material = material

    #Métodos comuns
    def trocaCor(self, cor): 
        print("Trocando cor...")
        self.__cor = cor
        return self.__cor
    
    def mostraCor(self):
        print(f"Cor da bola é {self.__cor}")

    #Property
    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
