from abc import ABC, abstractmethod
from typing import Optional
from modelo.barco import Barco

class Partida(ABC):

    @abstractmethod
    def disparar(self, x: int, y: int):
        pass
    
    
    @abstractmethod
    def obtener_tablero_propio(self, jugador: Optional[int] = None) -> list:
        pass
    
    
    @abstractmethod
    def obtener_tablero_rival(self, jugador: Optional[int] = None) -> list:
        pass
    
    
    @abstractmethod
    def colocar_barco(self, barco: Barco, x: Optional[int] = None, y: Optional[int] = None, horizontal: Optional[int] = None, jugador: Optional[int] = None) -> bool:
        pass
    

    @abstractmethod
    def hay_victoria(self):
        pass