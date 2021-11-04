class Forma:

    def __init__(self, base, altura): #Método constutor
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area

    def calcular_perimetro(self):
        perimetro = (self.base + self.altura) * 2 
        return perimetro

class Retangulo(Forma):

    def __init__(self, base, altura):
        super().__init__(base, altura) #função super com método da mãe

class Triangulo(Forma):

    def __init__(self, base, altura):
        super().__init__(base, altura)

    def calcular_area(self):
        area = (self.base * self.altura) / 2
        return area

    def calcular_perimetro(self):
        perimetro = (self.altura + self.altura) + self.base
        return perimetro
    
triangulo = Triangulo(4,8)
retangulo = Retangulo(4,8)

print(f"Area Triangulo: {int(triangulo.calcular_area())}")
print(f"Perimetro Triangulo: {triangulo.calcular_perimetro()}")

print(f"Area Retangulo: {retangulo.calcular_area()}")
print(f"Perimetro Retangulo: {retangulo.calcular_perimetro()}")

