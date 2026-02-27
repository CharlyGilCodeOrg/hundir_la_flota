from dominio.juego.juego import Juego

class JuegoPVP(Juego):
    def __init__(self, tablero_jugador1, tablero_jugador2, caracter_vacio, caracter_tocado, caracter_agua):
        """
        Inicializa una nueva partida PVP.

        :param tablero_jugador1: Objeto tablero para el jugador 1.
        :type tablero_jugador1: Tablero
        :param tablero_jugador2: Objeto tablero para el jugador 2.
        :type tablero_jugador2: Tablero
        :param caracter_vacio: Carácter para casillas vacías.
        :type caracter_vacio: str
        :param caracter_tocado: Carácter para disparos acertados.
        :type caracter_tocado: str
        :param caracter_agua: Carácter para disparos fallidos.
        :type caracter_agua: str
        """
        super().__init__(caracter_vacio, caracter_tocado, caracter_agua)
        self.tablero_jugador1 = tablero_jugador1
        self.tablero_jugador2 = tablero_jugador2
        self.turno_actual = 1  # 1 para jugador1, 2 para jugador2
        
    
    def cambiar_turno(self):
        """
        Cambia el turno entre los jugadores.
        """
        self.turno_actual = 2 if self.turno_actual == 1 else 1 
        
    
    def jugador_actual(self):
        """
        Devuelve el número del jugador actual.

        Returns:
            int: Número del jugador actual (1 o 2).
        """
        return self.turno_actual
        
        
    def disparar(self, x, y):
            """
            Realiza un disparo sobre el tablero del oponente.

            :param x: Coordenada X.
            :type x: int
            :param y: Coordenada Y.
            :type y: int
            :return: Resultado del disparo.
            :rtype: str
            """
            if self.turno_actual == 1:
                tablero_atacado = self.tablero_jugador2
                tablero_atacante = self.tablero_jugador1
            else:
                tablero_atacado = self.tablero_jugador1
                tablero_atacante = self.tablero_jugador2

            if tablero_atacante.disparo_repetido(
                x, y, self._caracter_tocado, self._caracter_agua
            ):
                return "REPETIDO"

            if tablero_atacado.comprobar_acierto(x, y):

                barco = tablero_atacado.obtener_barco_en_posicion(x, y)
                barco.recibir_impacto()

                tablero_atacado.marcar_disparo(x, y, self._caracter_tocado)
                tablero_atacante.marcar_disparo(x, y, self._caracter_tocado)

                if barco.hundido():
                    resultado = "TOCADO_Y_HUNDIDO"
                else:
                    resultado = "TOCADO"
            else:
                tablero_atacado.marcar_disparo(x, y, self._caracter_agua)
                tablero_atacante.marcar_disparo(x, y, self._caracter_agua)
                resultado = "AGUA"

            self.cambiar_turno()

            return resultado
        
        
    def hay_victoria(self):
        """
        Comprueba si quedan barcos en el tablero rival.

        :return: True si un jugador ha ganado, False si no.
        :rtype: bool
        """
        return not self.tablero_jugador1.quedan_barcos() or not self.tablero_jugador2.quedan_barcos()