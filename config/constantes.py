DIFICULTAD = {
    
    # Fácil
    1: {
        "ancho": 8,
        "alto": 8,
        "disparos": 60,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 1, "D"),
            (2, 1, "L"),
        ]
    },

    # Media (clásico)
    2: {
        "ancho": 10,
        "alto": 10,
        "disparos": 60,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 2, "D"),
            (2, 1, "L"),
        ]
    },

    # Difícil
    3: {
        "ancho": 10,
        "alto": 10,
        "disparos": 45,
        "barcos": [
            (5, 1, "P"),
            (4, 1, "A"),
            (3, 2, "D"),
            (2, 1, "L"),
        ]
    }
}

# Caracteres comunes
CARACTER_VACIO = "~"
CARACTER_TOCADO = "X"
CARACTER_AGUA = "O"
