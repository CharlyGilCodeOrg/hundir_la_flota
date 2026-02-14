import random

class Barco:
    """
    Representa un barco dentro del juego.
    """

    def __init__(self, tamanyo, cantidad, caracter):
        """
        Inicializa un barco con un tamaño y una orientación aleatoria.
        La vida restante es igual al tamaño y se va reduciendo en 1
        con cada disparo recibido.

        :param tamanyo: Tamaño del barco.
        :type tamanyo: int
        :param cantidad: Cantidad de barcos que se crearán.
        :type cantidad: int
        :param caracter: Carácter que representa al barco.
        :type caracter: str
        """
        self.tamanyo = tamanyo
        self.cantidad = cantidad
        self.caracter = caracter
        self.vida_restante = tamanyo
        self.horizontal = self.es_horizontal()


    def es_horizontal(self):
        """
        Determina aleatoriamente si la orientación del barco es horizontal o vertical.

        :return: True si es horizontal, False si es vertical.
        :rtype: bool
        """
        return random.choice([True, False])
    

    def calcular_maximo(self, alto_o_ancho):
        """
        Calcula el límite máximo para colocar un barco en un eje determinado.

        :param alto_o_ancho: Dimensión total del eje.
        :type alto_o_ancho: int
        :return: Posición máxima permitida.
        :rtype: int
        """
        return alto_o_ancho - self.tamanyo
    

    def queda_vida_restante(self):
        """
        Comprueba la vida restante del barco.
        
        :return: True si queda vida, False si no
        :rtype: bool
        """
        return self.vida_restante > 0