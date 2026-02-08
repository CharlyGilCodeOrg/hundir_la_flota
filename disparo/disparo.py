def disparo_acertado(array_original, array_copia, x, y):
    """
    Comprueba si un disparo ha impactado en un barco.

    :param array_original: Tablero visible para el jugador.
    :type array_original: list
    :param array_copia: Tablero interno con los barcos.
    :type array_copia: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :return: True si el disparo ha sido acertado, False en caso contrario.
    :rtype: bool
    """
    if array_copia[y][x] == "1":
        return True
    else:
        array_original[y][x] = "O"
        return False


def marcar_disparo(array_original, array_copia, x, y, caracter):
    """
    Marca un disparo en ambos tableros.

    :param array_original: Tablero visible para el jugador.
    :type array_original: list
    :param array_copia: Tablero interno.
    :type array_copia: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :param caracter: Carácter que representa el resultado del disparo.
    :type caracter: str
    :return: None
    """
    array_copia[y][x] = caracter
    array_original[y][x] = caracter


def disparo_repetido(array, x, y, caracter_tocado, caracter_agua):
    """
    Comprueba si el disparo se ha realizado sobre una casilla ya descubierta.

    :param array: Tablero visible para el jugador.
    :type array: list
    :param x: Coordenada X del disparo.
    :type x: int
    :param y: Coordenada Y del disparo.
    :type y: int
    :param caracter_tocado: Carácter que representa un disparo acertado.
    :type caracter_tocado: str
    :param caracter_agua: Carácter que representa un disparo fallido.
    :type caracter_agua: str
    :return: True si el disparo es repetido, False en caso contrario.
    :rtype: bool
    """
    return array[y][x] == caracter_tocado or array[y][x] == caracter_agua