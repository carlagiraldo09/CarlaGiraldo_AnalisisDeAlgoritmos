# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Carla Giraldo Camacho · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `91b900c`

Muy buen trabajo: la implementación es limpia y el informe se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 19 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 24 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **98 / 100** |
| **Nota (0–5)** | **4.90** |

## 1. Corrección conceptual (19 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, usando el ejemplo de 10, 24 y 17 con `m = 7`.
- Compara encadenamiento y direccionamiento abierto con ventajas y costos de cada uno.
- Justifica que la tabla no sirve para rangos y estima la altura y las comparaciones del árbol degenerado frente al equilibrado.
- Recomienda tabla hash más árbol equilibrado y declara con claridad que el valor a 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- Para el árbol equilibrado solo da el número de niveles; no explica de dónde sale ni compara con claridad el costo total frente al degenerado.
  → *Cómo corregirlo:* explique en una frase por qué la altura de un árbol equilibrado crece con el logaritmo de `n`, y ponga lado a lado las comparaciones totales de ambos casos.
- En la estimación a 5.000.000 supone que la tabla mantiene α cerca de 2 y no menciona otros efectos posibles de un tamaño tan grande (por ejemplo, la memoria).
  → *Cómo corregirlo:* añada una frase sobre qué podría hacer que el tiempo real de la tabla se aleje de lo estimado y por qué.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el `Θ(n)` de la lista porque debe revisar todos los nodos para confirmar que la guía no está.
- Nombra el supuesto de hash uniforme y explica que, si todas las guías caen en una casilla, la tabla vuelve a costar `Θ(n)`.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las dos estructuras devuelven el estado correcto en búsquedas exitosas e infructuosas, y la búsqueda de la lista es iterativa.
- La colisión forzada con `m = 7` funciona y `factor_carga` da `3 / 7`.
- Las pruebas comparan lista y tabla en 50 colecciones aleatorias (más de las 20 pedidas).
- La tabla reutiliza `ListaEnlazada` y no usa `dict`, `set` ni `hash()` en las estructuras.
- Todas las funciones tienen *docstrings* con `Args` y `Returns`, *type hints* y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (24 / 25)
**Lo que hizo bien:**
- Ambas gráficas tienen título, ejes rotulados, leyenda y las dos curvas en los mismos ejes; la primera cubre seis valores de `n` y la segunda seis valores de α.
- Los factores de crecimiento del informe (2,18 y 4,04 para la lista; cerca de 1 para la tabla) coinciden con sus tablas y con la forma de las gráficas.
- Compara bien lo medido con `Θ(n)` y con tiempo constante.

**Lo que puede mejorar (y cómo corregirlo):**
- Con la segunda gráfica dice que el aumento "es coherente" con `Θ(1 + α)`, pero no calcula qué crecimiento predice esa fórmula para comparar con el medido (3,58 veces).
  → *Cómo corregirlo:* calcule cuánto crece `1 + α` entre los dos valores de α que usó y compare ese número con el crecimiento del tiempo, comentando la diferencia.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` y sus archivos siguen la estructura pedida, y el `README.md` sigue el orden pedido.
- Las gráficas se incrustan con ruta relativa que sí apunta a archivos existentes.
- Cada parte práctica enlaza su código y hay instrucciones claras para reproducir.
- Hay tres commits descriptivos del laboratorio.

## ¿El código funciona?
Sí. Las pruebas pasan sin errores y `medicion.py` corre completo, imprime las tablas y genera las dos gráficas.
