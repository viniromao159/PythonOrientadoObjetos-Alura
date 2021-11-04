from collections.abc import Sized #Importa uma classe abstrata (ABC)

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao

    def __str__(self): 
        return self.descricao
    
    def __len__(self): #Método implementado para contagem
        return self.descricao

lista = MinhaListagem("Oi")
print(lista)