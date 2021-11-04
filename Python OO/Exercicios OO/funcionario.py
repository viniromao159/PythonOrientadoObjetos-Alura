
class Funcionario:

    def __init__(self, nome, salario) -> None:
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario