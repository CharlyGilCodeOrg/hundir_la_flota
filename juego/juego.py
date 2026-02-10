import disparo.disparo as disparo
import tablero.tablero as tablero
import barco.barco as barco
import utils.utils as util
import os

#Objetos
portaaviones = barco.Barco(4, 1, "P")
destructor = barco.Barco(3, 2, "D")
submarino = barco.Barco(2, 3, "S")
barcos = [portaaviones, destructor, submarino]
tablero_objeto = tablero.Tablero(10, 10)
validator = util.Util()

#Variables
tablero_usuario = [] # Array que se muestra al usuario con los disparos
tablero_barcos = [] # Array copia donde guardar las posiciones de los barcos
victoria = False # Banderas para saber cuándo finalizar los bucles
coordenadas_validas = False # Banderas para saber cuándo finalizar los bucles
contador = 0 # Contador para bucles
posicion_x = 0 # Coordenada X
posicion_y = 0 # Coordenada Y

# Constantes
CARACTER_TOCADO = "X"
CARACTER_AGUA = "O"
CARACTER_VACIO = "~"
CANTIDAD_DISPAROS = 50
MINIMO_RANDOM = 0 # Mínimo para el rango de valores aleatorios

class Juego:
    def generar_tableros(self, tablero, array_usuario, array_barcos, caracter):
        """
        Generar dos tableros, uno para mostrar al usuario (original)
        y otro para guardar los barcos (copia) y comparar los disparos 
        
        :param tablero: Tablero objeto
        :type tablero: Tablero
        :param array_usuario: Tablero visible para el jugador.
        :type array_usuario: list
        :param array_barcos: Tablero interno.
        :type array_barcos: list
        :param caracter_vacio: Carácter utilizado para inicializar cada celda.
        :type caracter_vacio: str
        :return: None
        """
        tablero.crear_tablero(array_usuario, caracter)
        tablero.crear_tablero(array_barcos, caracter)

    def obtener_caracteres_barco(self, barcos):
        """
        Obtiene una lista con los caracteres identificadores de los barcos.
        
        :param barcos: Lista de objetos Barco.
        :type barcos: list[Barco]
        :return: Lista de caracteres.
        :rtype: list
        """
        array_caracteres = []
        for barco in barcos:
            array_caracteres.append(barco.caracter)
        return array_caracteres

    def introducir_barcos(self, tablero, barcos, minimo, array_barcos):
        """
        Introducir barcos en el tablero interno.
        
        :param tablero: Tablero objeto.
        :type tablero: Tablero
        :param barcos: Lista de objetos Barco.
        :type barcos: list[Barco]
        :param minimo: Valor mínimo para las posiciones aleatorias.
        :type minimo: int
        :param array_barcos: Tablero interno.
        :type array_barcos: list
        :return: None
        """
        array_caracteres = self.obtener_caracteres_barco(barcos)
        for barco in barcos:
            tablero.generar_barcos(barco.cantidad, minimo, array_barcos, barco, array_caracteres)

    
    
