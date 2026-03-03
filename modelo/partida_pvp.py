from modelo.partida import Partida
from modelo.resultado import ResultadoDisparo

class PartidaPVP(Partida):

    def disparar(self, jugador, x, y):
        tablero_objetivo = self.obtener_tablero_rival(jugador)
        resultado = tablero_objetivo.recibir_disparo(x, y)

        if resultado != ResultadoDisparo.INVALIDO:
            self._cambiar_turno()

        return resultado
