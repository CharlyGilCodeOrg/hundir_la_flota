# 🚢 Hundir la Flota (Battleship)

## 1. 📄 Descripción del Proyecto

El objetivo es crear una versión digital del clásico juego de mesa **Hundir la Flota**. El programa jugará contra el usuario.

El ordenador esconderá varios barcos en un tablero y tú (el jugador) deberás adivinar sus coordenadas mediante disparos antes de que se te acabe la munición.

---

## 2. ⚙️ Especificaciones del Juego (Nivel Estándar)

### 🗺️ El Tablero

* Debe ser una **matriz de 10x10**.
* Al inicio, todo el tablero representa **mar desconocido**.

### 🚢 La Flota (Enemigos)

El programa debe colocar los siguientes barcos de forma **hardcoded (fija)** o **aleatoria (opcional)**:

* 1 Portaviones (**4 casillas**)
* 2 Submarinos (**3 casillas cada uno**)
* 3 Destructores (**2 casillas cada uno**)

**Regla importante:** los barcos **no pueden superponerse**.

---

### 🎮 Mecánica de Juego

1. El jugador comienza con **50 balas (intentos)**.
2. En cada turno, el programa solicita una **fila** y una **columna**.
3. El programa verifica el disparo:

   * **AGUA**: si no hay barco → se marca con `O`.
   * **TOCADO**: si hay un barco → se marca con `X`.
4. Después de cada disparo, se debe **mostrar el tablero actualizado** por pantalla.

---

## 3. 🛠️ Requisitos Técnicos

### ✅ Validación de Entradas

* El programa **no debe fallar (crash)** si el usuario introduce:

  * Coordenadas fuera del tablero (ej: fila 20).
  * Caracteres no válidos.
* En estos casos, se debe **pedir el dato de nuevo**.

### 🔁 Disparos Repetidos

* Si el usuario dispara a una casilla ya descubierta:

  * El programa debe **avisar**.
  * **No se debe restar una bala**.

### 🏁 Fin del Juego

* **Victoria**: se han hundido todos los barcos.
* **Derrota**: el contador de balas llega a 0.

---

## 4. 🧩 Opción Simplificada (Nivel Básico)

Si tienes dificultades con la versión estándar, puedes optar por esta versión reducida:

* **Tablero**: matriz de **5x5**.
* **Barcos**: 3 barcos de **1 sola casilla** cada uno.

  * No es necesario gestionar orientaciones.
* **Objetivo**: encontrar los 3 puntos escondidos en **menos de 10 intentos**.
* **Visualización**:

  * Es suficiente indicar por texto: `Agua`, `Tocado` o `Hundido`.
  * No es obligatorio imprimir el tablero completo en cada turno (aunque es recomendable).

---

## 5. 🖥️ Ejemplo de Visualización en Consola

```plaintext
--- TURNO ACTUAL: 5 ---
Munición restante: 45

  0 1 2 3 4 5 6 7 8 9
0 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
1 ~ O ~ ~ ~ ~ ~ ~ ~ ~
2 ~ ~ X X ~ ~ ~ ~ ~ ~
3 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
...

Introduce Fila (0-9): 3
Introduce Columna (0-9): 2
>>> ¡AGUA!
```

---

## 6. 📊 Criterios de Evaluación

| Concepto      | Descripción                                   | Peso |
| ------------- | --------------------------------------------- | ---- |
| Funcionalidad | El juego arranca y permite jugar turnos       | 30%  |
| Lógica        | Detecta correctamente Agua vs Tocado          | 30%  |
| Visualización | El tablero se actualiza correctamente         | 20%  |
| Robustez      | Control de errores (entradas inválidas)       | 10%  |
| Código Limpio | Variables bien nombradas y comentarios claros | 10%  |

---

💡 **Consejo**: trabaja siempre con ramas (`git checkout -b feature-juego`) y commits pequeños y descriptivos.

¡A hundir barcos! ⚓
