app/
   app.py 

config/
    constantes.py
    mensajes.py

modelo/
    partida/                    # 📁 Nuevo directorio
        __init__.py
        partida.py              # Clase abstracta/base
        partida_pve.py          # Implementación PVE
        partida_pvp.py          # Implementación PVP
        resultado.py            # (se mantiene aquí o dentro)
    barco.py
    tablero.py
    resultado.py                # O aquí si es usado por varias partidas

controlador/
    controlador.py              # Clase abstracta/base
    controlador_pve.py
    controlador_pvp.py

red/
    servidor.py
    cliente.py
    partida.py
    globales.py

vista/
    consola/
        __init__.py
        base/                   # 📁 Nuevo directorio
            __init__.py
            vista_consola.py    # Clase abstracta
        pve/
            __init__.py
            vista_consola_pve.py
        pvp/
            __init__.py
            vista_consola_pvp.py

utils/
    __init__.py
    validador.py
    excepciones.py

main.py