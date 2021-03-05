class Programa:
    def __init__(self, nome: str, ano: int):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'

    def __repr__(self):
        return f'Programa(nome={self.nome}, ano={self.ano}, likes={self.likes})'


class Filme(Programa):
    def __init__(self, nome: str, ano: int, duracao: int):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes}'

    def __repr__(self):
        return f'Programa(nome={self.nome}, ano={self.ano}, duracao={self.duracao}, likes={self.likes})'


class Serie(Programa):
    def __init__(self, nome: str, ano: int, temporadas: int):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes}'

    def __repr__(self):
        return f'Programa(nome={self.nome}, ano={self.ano}, temporadas={self.temporadas}, likes={self.likes})'


vingadores = Filme('vingadores', 2018, 160)
vingadores.dar_like()
# print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
atlanta.dar_like()
# print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')

filmes_series = [vingadores, atlanta]

for programa in filmes_series:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(programa)
