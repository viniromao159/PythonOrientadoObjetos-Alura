class Ingresso: #SuperClass 
    
    def __init__(self, valor): #Método constutor
        self.valor = valor

    def __str__(self): #Método representação textual
        return f"Valor ingresso: R${self.valor}"

class VIP(Ingresso):

    def __init__(self, valor, adicional): #Método constutor
        super().__init__(valor) #função super com método da mãe
        self.adicional = adicional

    def __str__(self): #Método representação textual
        return f"Valor ingresso VIP(+ Adicional R${self.adicional}): R${self.valor + self.adicional}"


ingresso_comum = Ingresso(15)
ingresso_vip = VIP(15,10)

ingressos = [ingresso_comum, ingresso_vip]

for valor_ingressos in ingressos: #imprimir ingressos 
    print(valor_ingressos)