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


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas


vingadores = Filme('vingadores', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
atlanta.dar_like()
atlanta.dar_like()
demolidor.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('Fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    # detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    print(programa)

print(f'Demolidor está ou não na lista: {demolidor in playlist_fim_de_semana}')
