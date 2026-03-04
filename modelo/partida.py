from abc import ABC, abstractmethod

class Partida(ABC):

    @abstractmethod
    def disparar(self, x: int, y: int):
        pass

    @abstractmethod
    def hay_victoria(self):
        pass
