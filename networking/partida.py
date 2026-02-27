class PartidaPVP:
    def __init__(self, player_1, player_2, tablero_1, tablero_2, turno_actual):
        """
        Constructor de la clase PartidaPVP

        Args:
            player_1 (str): Identificador del jugador 1.
            player_2 (str): Identificador del jugador 2.
            tablero_1 (Tablero): Tablero del jugador 1.
            tablero_2 (Tablero): Tablero del jugador 2.
            turno_actual (int): Entero que determina el turno (1 para turno jugador 1 y 2 para turno jugador 2)
        """
        self._player_1 = player_1
        self._player_2 = player_2
        self._tablero_1 = tablero_1
        self.tablero_2 = tablero_2
        self.turno_actual = turno_actual