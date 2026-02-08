from utils.utils import valor_aleatorio

def es_horizontal():
    """
    Determina aleatoriamente si la orientación es horizontal o vertical.

    :return: True si es horizontal, False si es vertical.
    :rtype: bool
    """
    if valor_aleatorio(0, 1) == 0:
        return True
    else:
        return False
