from abc import ABC  # abstract base classes
from collections.abc import MutableSequence, Sized
from numbers import Complex


class Playlist(MutableSequence):
    pass


class Numero(Complex):
    pass


class Listagem(Sized):
    pass


# filmes = Playlist()
# numeros = Numero()
listagem = Listagem()


