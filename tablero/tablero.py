import random

class Tablero:
    def __init__(self, ancho, alto):
        """
        Inicializa un tablero bidimensional.
        
        :param ancho: número de columnas.
        :param ancho: número de columnas.
        :type ancho: int
        :param alto: número de filas.
        :type alto: int
        """
        self.ancho = ancho
        self.alto = alto

    def crear_tablero(self, array, caracter_vacio):
        """
        Genera un tablero bidimensional (lista de listas) con las dimensiones indicadas.

        Cada posición del tablero se inicializa con el carácter especificado como vacío.

        :param array: Lista que contendrá el tablero generado.
        :type array: list
        :param caracter_vacio: Carácter utilizado para inicializar cada celda.
        :type caracter_vacio: str
        :return: None
        """
        for i in range(self.alto):
            fila = []
            for j in range(self.ancho):
                fila.append(caracter_vacio)
            array.append(fila)


    def rellenar_tablero(self, array, barco, x, y):
        """
        Introduce un barco en el tablero según la orientación indicada.

        El barco se coloca a partir de la posición (x, y) y ocupa tantas
        posiciones como indique su tamaño.

        :param array: Tablero donde se colocará el barco.
        :type array: list
        :param barco: Barco que se va a colocar en el tablero.
        :type barco: Barco
        :param x: Coordenada inicial en el eje X.
        :type x: int
        :param y: Coordenada inicial en el eje Y.
        :type y: int
        :return: None
        """
        if barco.horizontal:
            for i in range(barco.tamanyo):
                array[y][x] = barco.caracter
                x = x + 1
        else:
            for i in range(barco.tamanyo):
                array[y][x] = barco.caracter
                y = y + 1


    def ver_tablero(self, array):
        """
        Muestra por consola el tablero de juego con índices de filas y columnas.

        El tablero se imprime en formato matricial:
        - La primera línea muestra los índices de las columnas.
        - Cada fila se muestra precedida por su índice correspondiente.

        :param array: Tablero bidimensional a mostrar.
        :type array: list[list[str]]
        :return: None
        """
        encabezado = "   " + " ".join(str(i) for i in range(len(array[0])))
        print(encabezado)

        for i in range(self.alto):
            fila_str = f"{i:<2} " + " ".join(array[i])
            print(fila_str)


    def ya_hay_barco_en_posicion(self, array, barco, x, y, array_caracteres):
        """
        Comprueba si ya existe un barco en las posiciones donde se pretende colocar otro.

        :param array: Tablero donde se realiza la comprobación.
        :type array: list
        :param barco: Barco que se pretende colocar en el tablero.
        :type barco: Barco
        :param x: Coordenada inicial en el eje X.
        :type x: int
        :param y: Coordenada inicial en el eje Y.
        :type y: int
        :param array_caracteres: Lista de caracteres identificadores de los barcos.
        :type array_caracteres: list
        :return: True si hay un barco en alguna posición, False en caso contrario.
        :rtype: bool
        """
        if barco.horizontal:
            for i in range(barco.tamanyo):
                if array[y][x] in array_caracteres:
                    return True
                x = x + 1
        else:
            for i in range(barco.tamanyo):
                if array[y][x] in array_caracteres:
                    return True
                y = y + 1

        return False


    def quedan_barcos(self, array, array_caracteres):
        """
        Comprueba si quedan barcos sin hundir en el tablero.

        :param array: Tablero donde se realiza la comprobación.
        :type array: list
        :param array_caracteres: Lista de caracteres identificadores de los barcos.
        :type array_caracteres: list
        :return: True si quedan barcos, False si no.
        :rtype: bool
        """
        for i in range(self.alto):
            for j in range(self.ancho):
                if array[i][j] in array_caracteres:
                    return True
        return False


    def generar_barcos(self, minimo, array, barco, array_caracteres):
        """
        Genera y coloca un barcos aleatoriamente en el tablero.

        El proceso se repite hasta introducir el número de barcos 
        indicado en el atributo cantidad del objeto barco,
        comprobando que no se solapen entre sí.

        :param minimo: Valor mínimo para las posiciones aleatorias.
        :type minimo: int
        :param array: Tablero donde se colocan los barcos.
        :type array: list
        :param barco: Barco que se va a colocar en el tablero.
        :type barco: Barco
        :param array_caracteres: Lista de caracteres identificadores de los barcos.
        :type array_caracteres: list
        :return: None
        """
        contador = 0
        intentos_maximos = 1000
        intentos = 0

        while contador < barco.cantidad and intentos < intentos_maximos:
            intentos += 1
            barco.horizontal = barco.es_horizontal()

            max_x = barco.calcular_maximo(self.ancho)
            max_y = barco.calcular_maximo(self.alto)

            posicion_x = random.randint(minimo, max_x)
            posicion_y = random.randint(minimo, max_y)

            if not self.ya_hay_barco_en_posicion(array, barco, posicion_x, posicion_y, array_caracteres):
                self.rellenar_tablero(array, barco, posicion_x, posicion_y)
                contador = contador + 1
        
        if intentos == intentos_maximos:
            raise RuntimeError("No se pudieron colocar todos los barcos")
        

    def marcar_disparo(self, array_original, array_copia, disparo, caracter):
        """
        Marca un disparo en ambos tableros.

        :param array_original: Tablero visible para el jugador.
        :type array_original: list
        :param array_copia: Tablero interno.
        :type array_copia: list
        :param disparo: Disparo que se va a realizar en el tablero.
        :type disparo: Disparo
        :param caracter: Carácter que representa el resultado del disparo.
        :type caracter: str
        :return: None
        """
        array_copia[disparo.y][disparo.x] = caracter
        array_original[disparo.y][disparo.x] = caracter


    def disparo_repetido(self, array, disparo, caracter_tocado, caracter_agua):
        """
        Comprueba si el disparo se ha realizado sobre una casilla ya descubierta.

        :param array: Tablero visible para el jugador.
        :type array: list
        :param disparo: Disparo que se ha realizado en el tablero.
        :type disparo: Disparo
        :param caracter_tocado: Carácter que representa un disparo acertado.
        :type caracter_tocado: str
        :param caracter_agua: Carácter que representa un disparo fallido.
        :type caracter_agua: str
        :return: True si el disparo es repetido, False en caso contrario.
        :rtype: bool
        """
        return array[disparo.y][disparo.x] == caracter_tocado or array[disparo.y][disparo.x] == caracter_agua