"""
Interfaz de consola del juego Hundir la Flota.
"""
from utils.excepciones import VolverAlMenu
import os

class InterfazConsola:
    """
    Gestiona la interacción con el usuario por consola.
    """

    def __init__(self, textos, validador):
        """
        :param textos: Diccionario de textos del juego.
        :type textos: dict
        :param validador: Objeto validador.
        :type validador: Util
        """
        self.textos = textos
        self.validador = validador
    

    def pedir_disparo(self, ancho, alto):
        """
        Solicita al usuario las coordenadas del disparo.
        Permite escribir 'salir' para terminar el juego.

        :param ancho: Ancho del tablero.
        :type ancho: int
        :param alto: Alto del tablero.
        :type alto: int
        :return: El valor para X e Y introducido por el usuario
        :rtype: str
        """
        x = self._pedir_coordenada("x", ancho - 1)
        y = self._pedir_coordenada("y", alto - 1)
        return x, y


    def _pedir_coordenada(self, eje, limite):
        """
        Solicita una coordenada válida al usuario.
        99 es el valor establecido para terminar el programa.

        :param eje: Eje ('x' o 'y').
        :type eje: str
        :param limite: Valor máximo permitido.
        :type limite: int
        :return: Coordenada válida.
        :rtype: int
        :raises VolverAlMenu: Si el usuario selecciona la opción de salir.
        """
        valido = False
        while not valido:
            valor = input(self.textos[f"TEXTO_POSICION_{eje.upper()}"])
            print("")

            if valor.lower() == "salir":
                raise VolverAlMenu()

            if not self.validador.es_numero_entero(valor):
                print(self.textos["ERROR_NUMERO_ENTERO"])
                print("")
                continue

            if not self.validador.opcion_valida(valor, limite):
                print(self.textos["ERROR_LIMITE_TABLERO"])
                print("")
                continue
            
            valido = True
            return int(valor)


    def opcion_volver_menu(self):
        """
        Muestra el texto con la opción para volver al menú.
        """
        print("")
        print(self.textos["TEXTO_FIN_JUEGO"])
        print("")


    def fin_programa(self):
        """
        Muestra el texto de fin de programa.
        """
        print("")
        print(self.textos["FIN_DE_PROGRAMA"])
        print("")


    def mostrar_resultado(self, resultado):
        """
        Muestra el resultado del disparo.

        :param resultado: Resultado del disparo.
        :type resultado: str
        """
        print("")
        print(self.textos[f"TEXTO_{resultado}"])
        print("")


    def mostrar_tablero(self, tablero):
        """
        Muestra por consola el tablero de juego con índices de filas y columnas.

        El tablero se imprime en formato matricial:
        - La primera línea muestra los índices de las columnas.
        - Cada fila se muestra precedida por su índice correspondiente.

        :param tablero: Objeto tablero.
        :type tablero: Tablero
        """

        encabezado = "   " + " ".join(str(i) for i in range(len(tablero._casillas[0])))
        print(encabezado)

        for i in range(tablero.alto):
            fila_str = f"{i:<2} " + " ".join(tablero._casillas[i])
            print(fila_str)


    def mostrar_balas(self, restantes):
        """
        Muestra las balas restantes.

        :param restantes: Número de disparos restantes.
        :type restantes: int
        """
        print(self.textos["TEXTO_BALAS_RESTANTES"], restantes)


    def mostrar_mensaje_final(self, victoria):
        """
        Muestra el mensaje final del juego.

        :param victoria: Indica si el jugador ha ganado.
        :type victoria: bool
        """
        if victoria:
            print("")
            print(self.textos["TEXTO_VICTORIA"])
        else:
            print("")
            print(self.textos["TEXTO_DERROTA"])

        input(self.textos["PULSAR_ENTER"])


    def borrar_consola(self):
        """
        Borra lo escrito en la consola.
        """
        # \033[2J → limpia toda la pantalla
        # \033[H → mueve el cursor a la posición (0,0)
        print("\033[2J\033[H", end="")
        os.system('cls' if os.name == 'nt' else 'clear')


    
    def mostrar_instrucciones(self, instrucciones):
        """
        Muestra las instrucciones del juego.

        :param instrucciones: Instrucciones del juego.
        :type instrucciones: str
        """
        self.borrar_consola()
        print(instrucciones)
        input()
        self.borrar_consola()