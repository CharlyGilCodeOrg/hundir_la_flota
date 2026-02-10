"""
Módulo que contiene la clase Juego.
Gestiona la lógica principal de la partida.
"""

class Juego:
    """
    Controla el estado y las reglas del juego Hundir la Flota.
    """

    def __init__(self, tablero_usuario, tablero_barco, disparos_maximos, caracter_vacio, caracter_tocado, caracter_agua):
        """
        Inicializa una nueva partida.

        :param tablero_usuario: Objeto tablero para el usuario.
        :type tablero: Tablero
        :param tablero_barco: Objeto tablero interno.
        :type tablero: Tablero
        :param disparos_maximos: Número máximo de disparos permitidos.
        :type disparos_maximos: int
        :param caracter_vacio: Carácter para casillas vacías.
        :type caracter_vacio: str
        :param caracter_tocado: Carácter para disparos acertados.
        :type caracter_tocado: str
        :param caracter_agua: Carácter para disparos fallidos.
        :type caracter_agua: str
        """
        self.tablero_usuario = tablero_usuario
        self.tablero_barco = tablero_barco
        self.disparos_maximos = disparos_maximos
        self.disparos_realizados = 0

        self.caracter_vacio = caracter_vacio
        self.caracter_tocado = caracter_tocado
        self.caracter_agua = caracter_agua

        # Inicialización
        for barco in self.tablero_barco.barcos:
            self.tablero_barco.generar_barcos(barco)


    def disparar(self, x, y):
        """
        Realiza un disparo sobre el tablero.

        :param x: Coordenada X.
        :type x: int
        :param y: Coordenada Y.
        :type y: int
        :return: Resultado del disparo.
        :rtype: str
        """
        if self.tablero_usuario.disparo_repetido(
            x, y, self.caracter_tocado, self.caracter_agua
        ):
            return "REPETIDO"

        self.disparos_realizados += 1

        if self.tablero_barco.comprobar_acierto(x, y):
            self.tablero_barco.marcar_disparo(
                x,
                y,
                self.caracter_tocado
            )
            self.tablero_usuario.marcar_disparo(
                x,
                y,
                self.caracter_tocado
            )
            return "TOCADO"
        else:
            self.tablero_usuario.marcar_disparo(
                x,
                y,
                self.caracter_agua
            )
            return "AGUA"


    def quedan_disparos(self):
        """
        Indica si aún quedan disparos disponibles.

        :return: True si quedan disparos, False en caso contrario.
        :rtype: bool
        """
        return self.disparos_realizados < self.disparos_maximos


    def hay_victoria(self):
        """
        Comprueba si quedan barcos en el tablero interno.

        :return: True si no quedan barcos.
        :rtype: bool
        """
        return not self.tablero_barco.quedan_barcos()
