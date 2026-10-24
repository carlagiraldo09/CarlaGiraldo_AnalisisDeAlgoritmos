# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Carla Giraldo Camacho · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `adef10f`

Muy buen trabajo: el código es correcto y el análisis se apoya en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 14 / 20 |
| Calidad de la explicación teórica | 18 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **90 / 100** |
| **Nota (0–5)** | **4.50** |

## 1. Corrección conceptual (14 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara con el máximo de un arreglo, plantea `T(n) = 2T(n/2) + Θ(1)` y concluye que dividir no mejora `Θ(n)`.
- En la pregunta 5 recomienda divide y vencerás, declara que es una estimación y escala desde el tiempo medido en n = 4000 (no con regla de tres lineal).

**Lo que puede mejorar:**
- En la pregunta 3 no dice a partir de qué tamaño divide y vencerás empieza a ganar. Sus propios datos lo permiten: debía señalar ese tamaño o explicar por qué no aparece. La respuesta quedó general.
- Faltó apoyar esa respuesta con valores de los tamaños pequeños (por ejemplo, una tabla), ya que en la gráfica esos puntos no se distinguen.

## 2. Calidad de la explicación teórica (18 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Resuelve con el método maestro (caso 2) y justifica el `Θ(n²)` de la fuerza bruta con `n(n+1)/2` iteraciones.

**Lo que puede mejorar:**
- Al verificar la condición del caso, escriba la comparación completa: `f(n) = Θ(n^(log_b a))`, con `a`, `b` y `f(n)` explícitos.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos y coinciden en listas aleatorias.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista recibida.
- Tiene type hints y docstrings en las funciones.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 8 tamaños.
- Calcula el factor al duplicar n (3,94 y 2,08) y lo compara con lo esperado para `Θ(n²)` y `Θ(n log n)`. Esos valores coinciden con la gráfica publicada.

**Lo que puede mejorar:**
- Solo comparó un par de tamaños; con más pares el contraste sería más sólido.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, README en el orden pedido, enlaces al código, gráfica visible, instrucciones de reproducción y tres commits descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambas soluciones dan siempre la misma suma y la medición corre y regenera la gráfica sin errores.

## Para el próximo laboratorio
- Responda cada pregunta con el dato concreto que se pide (por ejemplo, el tamaño exacto del cruce de las curvas).
- Incluya una tabla con todos los tiempos medidos para poder analizar los tamaños pequeños.
- Mantenga los *type hints*, los *docstrings* con `Args` y `Returns` y las dos líneas en blanco entre funciones.
- Calcule el factor de crecimiento en más de un par de tamaños.
