from modelo.partida.partida import Partida
from modelo.tablero import Tablero
from modelo.barco import Barco
from modelo.resultado import ResultadoDisparo
from enum import Enum


class EstadoPartida(Enum):
    COLOCACION = "colocacion"
    JUGANDO = "jugando"
    FINALIZADA = "finalizada"


class PartidaPVP(Partida):

    def __init__(self, tablero_j1: Tablero, tablero_j2: Tablero) -> None:
        self._tableros = {
            1: tablero_j1,
            2: tablero_j2
        }

        self._turno = 1
        self._estado = EstadoPartida.COLOCACION

        self._jugadores_listos = set()


    def disparar(self, jugador: int, x: int, y: int) -> ResultadoDisparo:
        if self._estado != EstadoPartida.JUGANDO:
            raise ValueError("La partida no está en fase de juego")

        if jugador != self._turno:
            raise ValueError("No es tu turno")

        defensor = self._oponente(jugador)

        resultado, _ = self._tableros[defensor].recibir_disparo(x, y)

        if self._tableros[defensor].todos_hundidos():
            self._estado = EstadoPartida.FINALIZADA
        else:
            self._turno = defensor

        return resultado
    
    
    def obtener_tablero_propio(self, jugador: int) -> list:
        return self._tableros[jugador].ver_tablero()


    def obtener_tablero_rival(self, jugador: int) -> list:
        rival = self._oponente(jugador)
        return self._tableros[rival].ver_tablero_rival()
    
    
    def colocar_barco(self, barco :Barco, x: int, y: int, horizontal: bool, jugador: int) -> bool:
        if self._estado != EstadoPartida.COLOCACION:
            raise ValueError("La fase de colocación ha terminado")

        tablero = self._tableros[jugador]
        barco.set_horizontal(horizontal)
        colocado = tablero.colocar_barco_manual(barco, x, y)

        if colocado:
            if tablero.todos_colocados():
                self._jugadores_listos.add(jugador)

                if len(self._jugadores_listos) == 2:
                    self._estado = EstadoPartida.JUGANDO
                    self._turno = 1

        return colocado
    
    
    def hay_victoria(self) -> bool:
        return self._estado == EstadoPartida.FINALIZADA


    def estado(self) -> EstadoPartida:
        return self._estado


    def turno_actual(self) -> int:
        return self._turno
    
    
    def jugador_ganador(self) -> int | None:
        if self._estado != EstadoPartida.FINALIZADA:
            return None

        for jugador in (1, 2):
            if self._tableros[self._oponente(jugador)].todos_hundidos():
                return jugador

        return None


    def _oponente(self, jugador: int) -> int:
        return 2 if jugador == 1 else 1

