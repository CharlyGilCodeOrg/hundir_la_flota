import disparo.disparo as disparo
import tablero.tablero as tablero
import utils.utils as utils
import os

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
tablero.crear_tablero(array_original, ANCHO, ALTO, CARACTER_VACIO)
tablero.crear_tablero(array_copia, ANCHO, ALTO, CARACTER_VACIO)

# Introducir Portaaviones
tablero.generar_barcos(contador, 1, fin_de_bucle, MINIMO_RANDOM, TAMANYO_PORTA, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)
# Introducir Submarinos
tablero.generar_barcos(contador, 2, fin_de_bucle, MINIMO_RANDOM, TAMANYO_SUBMA, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)
# Introducir Destructores
tablero.generar_barcos(contador, 3, fin_de_bucle, MINIMO_RANDOM, TAMANYO_DESTRUC, ANCHO, ALTO, array_copia, CARACTER_POSICION_BARCO)

# Bucle que se repite mientras queden disparos y barcos
while contador < CANTIDAD_DISPAROS and not victoria:
    # Mientras los valores no sean válidos, repetir bucle anidado
    while not coordenadas_validas: 
        print("")
        posicion_x = input(TEXTO_POSICION_X) # Pedir coordenada x

        if not utils.es_numero_entero(posicion_x): # Comprobar si es número entero
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            if not utils.opcion_valida(posicion_x, ANCHO - 1): # Comprobar si el valor está dentro del límte del tablero
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO) 
                continue
        
        print("")
        posicion_y = input(TEXTO_POSICION_Y)  # Pedir coordenada y

        if not utils.es_numero_entero(posicion_y): # Comprobar si es número entero
            print("")
            print("ERROR:", ERROR_NUMERO_ENTERO)
            continue
        else:
            if not utils.opcion_valida(posicion_y, ALTO - 1): # Comprobar si el valor está dentro del límte del tablero
                print("")
                print("ERROR:", ERROR_LIMITE_TABLERO)
                continue
        
        coordenadas_validas = True # Si llega hasta aquí, es que los valores son válidos, y termina el bucle anidado

    os.system('cls') # Borrar consola

    if disparo.disparo_repetido(array_original, int(posicion_x), int(posicion_y), CARACTER_TOCADO, CARACTER_AGUA): # Comprobar si ya se había disparado en esta casilla
        print("")
        print(TEXTO_REPETIDO)
        print("")
        print(TEXTO_BALAS_RESTANTES, CANTIDAD_DISPAROS - contador) # Mostrar mensaje con las balas restantes
        print("")
        coordenadas_validas = False
        tablero.ver_tablero(array_original, ALTO)
        print("")
        continue

    if disparo.disparo_acertado(array_original, array_copia, int(posicion_x), int(posicion_y)): # Comprobar si se ha acertado en un barco
        disparo.marcar_disparo(array_original, array_copia, int(posicion_x), int(posicion_y), CARACTER_TOCADO)
        print("")
        print(TEXTO_TOCADO)
        if not tablero.quedan_barcos(array_copia, ANCHO, ALTO): # Comprobar si quedan barcos
            victoria = True
    else:
        disparo.marcar_disparo(array_original, array_copia, int(posicion_x), int(posicion_y), CARACTER_AGUA)
        print(TEXTO_AGUA)

    if contador < CANTIDAD_DISPAROS:
        coordenadas_validas = False # Reinciar bandera si quedan disparos para volver a pedir coordenadas

    contador = contador + 1

    # Descomentar la siguiente sección para ver el array con los barcos
    # print("")
    # print("BARCOS")
    # print("")
    # tablero.ver_tablero(array_copia, ALTO)

    print("")
    tablero.ver_tablero(array_original, ALTO) # Mostrar tablero con los disparos efectuados
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