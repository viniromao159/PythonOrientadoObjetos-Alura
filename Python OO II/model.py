class Programa: #Super class -> Classe mãe que herda a outra classes
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self) -> str:
        return f"Nome:{self.nome} - Likes:{self.likes}"

    def dar_likes(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

class Filme(Programa): #Classe herdeira, recebendo a superclass como parametro para indentifica-lo como
    def __init__(self, nome, ano, duracao) -> None:
        super().__init__(nome,ano)
        self.duracao = duracao
    
    def __str__(self) -> str: #Método para representar a classe de forma textual
        return f"Nome: {self.nome} - Duração: {self.duracao}min - Likes: {self.likes}"

class Serie(Programa):
    def __init__(self, nome, ano, temporadas) -> None:
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self) -> str:
        return f"Nome: {self.nome} - Temporadas: {self.temporadas} - Likes: {self.likes}"

class Playlist: 
    
    def __init__(self, nome, programas) -> None:
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):#Considera o objeto como iterable
        return self._programas[item]
    
    @property  #Transforma o objeto em iterable
    def listagem(self):
        return self._programas

    @property #Permite a contagem da lista
    def tamanho(self):
        return len(self._programas)
    

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
v_de_vingança = Filme('V de vingança!', 2005, 132)
watch_men = Filme('Watch-men', 2009, 180)

v_de_vingança.dar_likes()
watch_men.dar_likes()
watch_men.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filmesseries = [vingadores, atlanta, v_de_vingança, watch_men] #List dos objetos
filmes_fds = Playlist("Fim de semana!", filmesseries)#Criando objeto adicionando a list como parametro

for programa in filmes_fds: #Chama os atributo do objeto
    print(programa)

print(f'Tamanho: {filmes_fds.tamanho}')   

