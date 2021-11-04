
class Datas:

    def __init__(self, dia, mes, ano) -> None:
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def formata_brasil(self):
        print(f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano}")

    def formata_eua(self):
        print(f"{self.__mes:02d}-{self.__dia:02d}-{self.__ano}")

