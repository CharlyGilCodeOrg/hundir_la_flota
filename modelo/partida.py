from abc import ABC, abstractmethod

class Partida(ABC):

    @abstractmethod
    def disparar(self, jugador, x, y):
        pass

    @abstractmethod
    def hay_victoria(self):
        pass
