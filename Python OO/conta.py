
class Conta:

    def __init__(self,numero,titular,saldo,limite): #Método construtor
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    #Métodos
    def extrato(self):
        print(f"Extrato -> Titular : {self.titular} / Conta: {self.__numero} / Saldo: {self.__saldo}")

    def deposita(self, valor):
        print("Depositando valor...")
        self.__saldo += valor
    
    def saca(self, valor):
        self.__saldo -= valor  

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def __saldo_saque(self, valor): #Método privado -> valida o valor de saque
        if (self.saca <= self.__saldo + self.__limite):
           self._saldo -= valor
        else:
            ("Valor indisponivel para saque!")

    #Propriedades
    @property #retorna com @property / substitui o get_
    def titular(self):
        return self.__titular.title()
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter #altera com @atributo.setter / substitui o set_
    def limite(self, limite):
        print("Alterando limite...")
        self.__limite = limite

    @staticmethod #Método Statico 
    def codigo_banco():
        return "001"
    
    @staticmethod #Método Statico 
    def codigos_bancos():
        return {"BB":"001", "CAIXA":"104", "Bradesco":"237" }