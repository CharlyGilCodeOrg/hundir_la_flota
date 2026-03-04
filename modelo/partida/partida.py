from abc import ABC, abstractmethod

class Partida(ABC):

    @abstractmethod
    def disparar(self, x: int, y: int):
        pass

    @abstractmethod
    def hay_victoria(self):
        pass

# Falta método obtener_tablero_propio
# Falta método obtener_tablero_rival
# Falta método colocar_barco?