
class Combustivel:

    def __init__(self, tipo_combustivel, valor_litro, quantidade_litro):#Método construtor
        self.__tipo_combustivel = tipo_combustivel
        self.__valor_litro = valor_litro
        self.__quantidade_litro = quantidade_litro

    def abastecer_valor(self, valor):#Método retorna quantidade de litro pelo valor colocado
        litro =  valor / self.__valor_litro
        self.__quantidade_litro -= litro
        return litro
    
    def abastecer_litro(self, litro):#Método retorna o valor a ser pago pelo litro colocado
        valor = litro * self.__valor_litro
        self.__quantidade_litro -= litro
        return valor
    
    def get_quantidade(self):#Retorna a quantidade de litro na bomba
        return self.__quantidade_litro
    
    #Altera os valores dos atributos
    def set_valor_litro(self, valor):
        self.__valor_litro = valor
    
    def set_tipo_combustivel(self, tipo):
        self.__tipo_combustivel = tipo
    
    def set_quantidade_combustivel(self, quantidade):
        self.__quantidade_litro = quantidade

