
class Retangulo:

    def __init__(self) -> None:
        self.__ladoA = float(input("Digite o valor do lado maior: "))
        self.__ladoB = float(input("Digite o valor do lado menor: "))

    def calcularArea (self):
        print("Calculando Area...")
        return self.__ladoA * self.__ladoB
        
    
    def calcularPerimetro(self):
        print("Calculando Perimetro...")
        return (self.__ladoA*2) + (self.__ladoB*2)

    def get_lados(self):
        return f"Lado A: {self.__ladoA} - Lado B: {self.__ladoB}"

    def set_lados(self, ladoA, ladoB): #Método Set com opção de troca
            self.__ladoA = float("Digite o tamanho do lado maior: ")
            self.__ladoB = float("Digite o tamanho do lado menor: ")
            print("Troca efetuada!")
