import random
import os

###########
# MÉTODOS #
###########

# Genera un array bidimensional en función del ancho y alto introducidos
def crear_tablero(array, ancho, alto, caracter_vacio):
        for i in range(alto):
            fila = []
            for j in range(ancho):
                fila.append(caracter_vacio)
            array.append(fila)

# Genera un valor aleatorio para un rango dado
def valor_aleatorio(menor, mayor):
    return random.randint(menor, mayor)

# Establece si la posición es horizontal o vertical de forma aleatoria
def es_horizontal():
    if valor_aleatorio(0, 1) == 0:
        return True
    else:
        return False

# Introduce un barco dentro del array
def rellenar_tablero(array, horizontal, tamanyo, x, y, caracter_barco):
        if horizontal:
            for i in range(tamanyo):
                array[y][x] = caracter_barco
                x = x + 1
        else:
            for i in range(tamanyo):
                array[y][x] = caracter_barco
                y = y + 1

# Imprime por consola el tablero
def ver_tablero(array, alto):
    for i in range(alto):
        print(array[i])

# Comprueba si la opción introducida es un entero dentro del rango
def opcion_valida(valor, opcion_maxima):
    return valor.isdigit() and 0 <= int(valor) <= opcion_maxima

# Comprueba si el valor introducido es un número entero
def es_numero_entero(valor):
    try:
        int(valor)
        return True
    except ValueError:
        return False

# Calcula el límite para los ejes x o y 
def calcular_maximos(tamanyo, alto_o_ancho):
    return alto_o_ancho - tamanyo


# Comprueba que la posicón dada no supere el límite
# El límite se obtiene en calcular_maximos()
def posicion_valida(posicion, maximo):
    if posicion <= maximo:
        return True
    else:
        return False

# Comprueba si hay un 1 (barco) en las posiciones del array copia
def ya_hay_barco_en_posicion(array, horizontal, tamanyo, x, y, caracter_barco):
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

# Comprobar si el disparo ha dado en un barco
def disparo_acertado(array_original, array_copia, x, y):
    if array_copia[y][x] == "1":
        return True
    else:
        array_original[y][x] = "O"
        return False
    
# Marcar con fallo o acierto los arrays
def marcar_disparo(array_original, array_copia, x, y, caracter):
    array_copia[y][x] = caracter
    array_original[y][x] = caracter
    
# Comprobar si el disparo ha dado en una casilla ya descubierta
def disparo_repetido(array, x, y, caracter_tocado, caracter_agua):
    return array[y][x] == caracter_tocado or array[y][x] == caracter_agua

# Comprobar si quedan barcos sin hundir
def quedan_barcos(array, ancho, alto):
    for i in range(alto):
        for j in range(ancho):
            if array[i][j] == "1":
                return True
    return False

# Función para generar barcos
def bucle_generar_barcos(contador, repeticiones, bandera, minimo, tamanyo, ancho, alto, array, caracter_barco):
    while contador < repeticiones: # Se introducen x barcos, hasta que no se introduzcan se repite el bucle
        horizontal = es_horizontal()

        while not bandera: # Bucle anidado que se repite hasta que la bandera está en True
            posicion_x = valor_aleatorio(minimo, calcular_maximos(tamanyo, ancho))
            posicion_y = valor_aleatorio(minimo, calcular_maximos(tamanyo, alto))
            if not ya_hay_barco_en_posicion(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco): # Comprobar si hay barco en las posiciones dadas
                rellenar_tablero(array, horizontal, tamanyo, posicion_x, posicion_y, caracter_barco) # Si no lo hay, introducir barco
                contador = contador + 1 # Contador del bucle principal
                if contador == repeticiones:
                    bandera = True # Fin del bucle

    bandera = False # Reiniciar bandera y contador para próximos usos
    contador = 0


########
# MAIN #
########

#Variables
array_original = [] # Array que se muestra al usuario con los disparos
array_copia = [] # Array copia donde guardar las posiciones de los barcos
fin_de_bucle = False # Banderas para saber cuándo finalizar los bucles
victoria = False # Banderas para saber cuándo finalizar los bucles
coordenadas_validas = False # Banderas para saber cuándo finalizar los bucles
horizontal = False # Booleano que marca si el barco se introduce en horizontal o vertical
contador = 0 # Contador para bucles
posicion_x = 0 # Coordenada X
posicion_y = 0 # Coordenada Y

# Constantes
CARACTER_TOCADO = "X"
CARACTER_AGUA = "O"
CARACTER_VACIO = "~"
CARACTER_POSICION_BARCO = "1"
CANTIDAD_DISPAROS = 50
MINIMO_RANDOM = 0 # Mínimo para el rango de valores aleatorios
TAMANYO_PORTA = 4 
TAMANYO_SUBMA = 3 
TAMANYO_DESTRUC = 2 
ANCHO = 10 # Dimensiones del tablero
ALTO = 10 # Dimensiones del tablero
# Textos para los inputs
TEXTO_POSICION_X = "Introduzca la coordenada x: "
TEXTO_POSICION_Y = "Introduzca la coordenada y: "
# Textos para disparos
TEXTO_TOCADO = "TOCADO"
TEXTO_AGUA = "AGUA"
TEXTO_REPETIDO = "YA HABÍAS DISPARADO EN ESTE HUECO. NO PIERDES LA BALA."
TEXTO_BALAS_RESTANTES = "BALAS RESTANTES: "
# Textos victoria/derrota
TEXTO_VICTORIA = "TE HAS CARGADO TODOS LOS BARCOS, ENHORABUENA."
TEXTO_DERROTA = "LÁSTIMA, TE HAS QUEDADO SIN BALAS. AFINA TU PUNTERÍA Y VUELVE A INTENTARLO."
# Textos de error 
ERROR_LIMITE_TABLERO = "La posición del disparo excede los límites del tablero"
ERROR_NUMERO_ENTERO =  "Introduce números enteros, por favor"

# Generar dos tableros, uno para mostrar al usuario (original) 
# y otro para guardar los barcos (copia) y comparar con los disparos
crear_tablero(array_original, ANCHO, ALTO, CARACTER_VACIO)
crear_tablero(array_copia, ANCHO, ALTO, CARACTER_VACIO)

# Introducir Portaaviones
bucle_generar_barcos(contador, 1, fin_de_bucle, MINIMO_RANDOM, TAMANYO_PORTA, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)
# Introducir Submarinos
bucle_generar_barcos(contador, 2, fin_de_bucle, MINIMO_RANDOM, TAMANYO_SUBMA, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)
# Introducir Destructores
bucle_generar_barcos(contador, 3, fin_de_bucle, MINIMO_RANDOM, TAMANYO_DESTRUC, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)

# Bucle que se repite mientras queden disparos y barcos
while contador < CANTIDAD_DISPAROS and not victoria:
    # Mientras los valores no sean válidos, repetir bucle anidado
    while not coordenadas_validas: 
        print("")
        posicion_x = input(TEXTO_POSICION_X) # Pedir coordenada x

        # Comprobar si es número entero
        if not es_numero_entero(posicion_x): 
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            # Comprobar si el valor está dentro del límte del tablero
            if not opcion_valida(posicion_x, ANCHO - 1): 
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO) 
                continue
        
        print("")
        posicion_y = input(TEXTO_POSICION_Y)  # Pedir coordenada y

        # Comprobar si es número entero
        if not es_numero_entero(posicion_y): 
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            # Comprobar si el valor está dentro del límte del tablero
            if not opcion_valida(posicion_y, ALTO - 1): 
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO)
                continue
        
        coordenadas_validas = True # Si llega hasta aquí, es que los valores son válidos, y termina el bucle anidado

    os.system('cls') # Borrar consola

    # Comprobar si ya se había disparado en esta casilla
    if disparo_repetido(array_original, int(posicion_x), int(posicion_y), CARACTER_TOCADO, CARACTER_AGUA):
        print("")
        print(TEXTO_REPETIDO)
        print("")
        print(TEXTO_BALAS_RESTANTES, CANTIDAD_DISPAROS - contador) # Mostrar mensaje con las balas restantes
        print("")
        coordenadas_validas = False
        ver_tablero(array_original, ALTO)
        print("")
        continue

    # Comprobar si se ha acertado en un barco
    if disparo_acertado(array_original, array_copia, int(posicion_x), int(posicion_y)): 
        marcar_disparo(array_original, array_copia, int(posicion_x), int(posicion_y), CARACTER_TOCADO)
        print("")
        print(TEXTO_TOCADO)
        # Comprobar si quedan barcos
        if not quedan_barcos(array_copia, ANCHO, ALTO): 
            victoria = True
    else:
        marcar_disparo(array_original, array_copia, int(posicion_x), int(posicion_y), CARACTER_AGUA)
        print(TEXTO_AGUA)

    if contador < CANTIDAD_DISPAROS:
        coordenadas_validas = False # Reinciar bandera si quedan disparos para volver a pedir coordenadas

    contador = contador + 1

    # Descomentar la siguiente sección para ver el array con los barcos
    # print("")
    # print("BARCOS")
    # print("")
    # ver_tablero(array_copia, ALTO)

    print("")
    ver_tablero(array_original, ALTO) # Mostrar tablero con los disparos efectuados
    print("")
    print(TEXTO_BALAS_RESTANTES, CANTIDAD_DISPAROS - contador) # Mostrar mensaje con las balas restantes
    
if victoria:
    print("")
    print(TEXTO_VICTORIA)
    print("")
else:
    print("")
    print(TEXTO_DERROTA)
    print("")
