"""
Interfaz de consola del juego Hundir la Flota.
"""
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


    def pedir_coordenada(self, eje, limite):
        """
        Solicita una coordenada válida al usuario.
        99 es el valor establecido para terminar el programa.

        :param eje: Eje ('x' o 'y').
        :type eje: str
        :param limite: Valor máximo permitido.
        :type limite: int
        :return: Coordenada válida.
        :rtype: int
        """
        valido = False
        while not valido:
            valor = input(self.textos[f"TEXTO_POSICION_{eje.upper()}"])
            print("")

            if not self.validador.es_numero_entero(valor):
                print(self.textos["ERROR_NUMERO_ENTERO"])
                print("")
                continue

            if int(valor) == 99:
                return None

            if not self.validador.opcion_valida(valor, limite):
                print(self.textos["ERROR_LIMITE_TABLERO"])
                print("")
                continue
            
            valido = True
            return int(valor)


    def opcion_fin_programa(self):
        """
        Muestra el texto con la opción para terminar el programa.

        """
        print(self.textos["TEXTO_FIN_PROGRAMA"])
        print("")

    def fin_programa(self):
        """
        Muestra el texto de fin de programa.

        """
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
        print("")
        print(self.textos["TEXTO_BALAS_RESTANTES"], restantes)
        print("")


    def mostrar_mensaje_final(self, victoria):
        """
        Muestra el mensaje final del juego.

        :param victoria: Indica si el jugador ha ganado.
        :type victoria: bool
        """
        if victoria:
            print(self.textos["TEXTO_VICTORIA"])
            print("")
        else:
            print(self.textos["TEXTO_DERROTA"])
            print("")


    def borrar_consola(self):
        """
        Borra lo escrito en la consola
        
        """
        os.system('cls')