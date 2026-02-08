from barco.barco import es_horizontal
from utils.utils import valor_aleatorio

def crear_tablero(array, ancho, alto, caracter_vacio):
    """
    Genera un tablero bidimensional (lista de listas) con las dimensiones indicadas.

    Cada posición del tablero se inicializa con el carácter especificado como vacío.

    :param array: Lista que contendrá el tablero generado.
    :type array: list
    :param ancho: Número de columnas del tablero.
    :type ancho: int
    :param alto: Número de filas del tablero.
    :type alto: int
    :param caracter_vacio: Carácter utilizado para inicializar cada celda.
    :type caracter_vacio: str
    :return: None
    """
    for i in range(alto):
        fila = []
        for j in range(ancho):
            fila.append(caracter_vacio)
        array.append(fila)


def rellenar_tablero(array, horizontal, tamanyo, x, y, caracter_barco):
    """
    Introduce un barco en el tablero según la orientación indicada.

    El barco se coloca a partir de la posición (x, y) y ocupa tantas
    posiciones como indique su tamaño.

    :param array: Tablero donde se colocará el barco.
    :type array: list
    :param horizontal: Indica si el barco se coloca horizontalmente.
    :type horizontal: bool
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param x: Coordenada inicial en el eje X.
    :type x: int
    :param y: Coordenada inicial en el eje Y.
    :type y: int
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: None
    """
    if horizontal:
        for i in range(tamanyo):
            array[y][x] = caracter_barco
            x = x + 1
    else:
        for i in range(tamanyo):
            array[y][x] = caracter_barco
            y = y + 1


def calcular_maximos(tamanyo, alto_o_ancho):
    """
    Calcula el límite máximo para colocar un barco en un eje determinado.

    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param alto_o_ancho: Dimensión total del eje.
    :type alto_o_ancho: int
    :return: Posición máxima permitida.
    :rtype: int
    """
    return alto_o_ancho - tamanyo


def ver_tablero(array, alto):
    """
    Muestra por consola el tablero de juego con índices de filas y columnas.

    El tablero se imprime en formato matricial:
    - La primera línea muestra los índices de las columnas.
    - Cada fila se muestra precedida por su índice correspondiente.

    :param array: Tablero bidimensional a mostrar.
    :type array: list[list[str]]
    :param alto: Número de filas del tablero.
    :type alto: int
    :return: None
    """
    encabezado = "   " + " ".join(str(i) for i in range(len(array[0])))
    print(encabezado)

    for i in range(alto):
        fila_str = f"{i:<2} " + " ".join(array[i])
        print(fila_str)


def ya_hay_barco_en_posicion(array, horizontal, tamanyo, x, y, caracter_barco):
    """
    Comprueba si ya existe un barco en las posiciones donde se pretende colocar otro.

    :param array: Tablero donde se realiza la comprobación.
    :type array: list
    :param horizontal: Orientación del barco.
    :type horizontal: bool
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param x: Coordenada inicial en el eje X.
    :type x: int
    :param y: Coordenada inicial en el eje Y.
    :type y: int
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: True si hay un barco en alguna posición, False en caso contrario.
    :rtype: bool
    """
    if horizontal:
        for i in range(tamanyo):
            if array[y][x] == caracter_barco:
                return True
            x = x + 1
    else:
        for i in range(tamanyo):
            if array[y][x] == caracter_barco:
                return True
            y = y + 1

    return False


def quedan_barcos(array, ancho, alto):
    """
    Comprueba si quedan barcos sin hundir en el tablero.

    :param array: Tablero donde se realiza la comprobación.
    :type array: list
    :param ancho: Número de columnas del tablero.
    :type ancho: int
    :param alto: Número de filas del tablero.
    :type alto: int
    :return: True si quedan barcos, False si no.
    :rtype: bool
    """
    for i in range(alto):
        for j in range(ancho):
            if array[i][j] == "1":
                return True
    return False


def generar_barcos(contador, repeticiones, bandera, minimo, tamanyo, ancho, alto, array, caracter_barco):
    """
    Genera y coloca barcos aleatoriamente en el tablero.

    El proceso se repite hasta introducir el número de barcos indicado,
    comprobando que no se solapen entre sí.

    :param contador: Contador interno del número de barcos colocados.
    :type contador: int
    :param repeticiones: Número total de barcos a generar.
    :type repeticiones: int
    :param bandera: Bandera de control del bucle.
    :type bandera: bool
    :param minimo: Valor mínimo para las posiciones aleatorias.
    :type minimo: int
    :param tamanyo: Tamaño del barco.
    :type tamanyo: int
    :param ancho: Ancho del tablero.
    :type ancho: int
    :param alto: Alto del tablero.
    :type alto: int
    :param array: Tablero donde se colocan los barcos.
    :type array: list
    :param caracter_barco: Carácter que representa al barco.
    :type caracter_barco: str
    :return: None
    """
    while contador < repeticiones:
        horizontal = es_horizontal()

        while not bandera:
            posicion_x = valor_aleatorio(minimo, calcular_maximos(tamanyo, ancho))
            posicion_y = valor_aleatorio(minimo, calcular_maximos(tamanyo, alto))
            if not ya_hay_barco_en_posicion(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco):
                rellenar_tablero(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco)
                contador = contador + 1
                if contador == repeticiones:
                    bandera = True

    bandera = False
    contador = 0