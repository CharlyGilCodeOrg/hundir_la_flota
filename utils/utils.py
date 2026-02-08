import random

def opcion_valida(valor, opcion_maxima):
    """
    Comprueba si un valor introducido es un número entero dentro de un rango válido.

    :param valor: Valor introducido por el usuario.
    :type valor: str
    :param opcion_maxima: Valor máximo permitido.
    :type opcion_maxima: int
    :return: True si el valor es válido, False en caso contrario.
    :rtype: bool
    """
    return valor.isdigit() and 0 <= int(valor) <= opcion_maxima


def es_numero_entero(valor):
    """
    Comprueba si un valor puede convertirse a número entero.

    :param valor: Valor a comprobar.
    :type valor: str
    :return: True si el valor es un entero válido, False en caso contrario.
    :rtype: bool
    """
    try:
        int(valor)
        return True
    except ValueError:
        return False


def posicion_valida(posicion, maximo):
    """
    Comprueba si una posición se encuentra dentro del límite permitido.

    :param posicion: Posición a comprobar.
    :type posicion: int
    :param maximo: Valor máximo permitido.
    :type maximo: int
    :return: True si la posición es válida, False en caso contrario.
    :rtype: bool
    """
    if posicion <= maximo:
        return True
    else:
        return False
    

def valor_aleatorio(menor, mayor):
    """
    Genera un número entero aleatorio dentro de un rango dado.

    :param menor: Valor mínimo del rango.
    :type menor: int
    :param mayor: Valor máximo del rango.
    :type mayor: int
    :return: Número entero aleatorio entre menor y mayor (ambos incluidos).
    :rtype: int
    """
    return random.randint(menor, mayor)