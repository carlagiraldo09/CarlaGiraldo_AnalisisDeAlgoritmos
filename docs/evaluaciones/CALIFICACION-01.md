# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Carla Giraldo Camacho · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-13 23:59 · **Versión revisada:** commit `7bfe8e4`

Muy buen trabajo: su informe está completo y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 22 / 25 |
| Corrección de la implementación | 18 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **89 / 100** |
| **Nota (0–5)** | **4.45** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el resultado sea correcto y que llegue a tiempo, y nombra la restricción incumplida: la ventana de cuatro horas.
- Explica por qué un servidor el doble de rápido solo gana un factor fijo de 2 frente a un crecimiento cuadrático.
- Su segundo ejemplo (la fusión de dos bancos) trae datos y una ventana de tiempo concretos.
- En la parte ética identifica al paciente y al operador del centro de contacto, y dice quién asume cada costo.

**Lo que puede mejorar:**
- En la parte ambiental falta convertir las horas de ejecución en una cifra aproximada de energía (por ejemplo, potencia del servidor por horas por días del año).
- La obligación que impone que el orden de la lista decida a quién se llama primero queda apenas esbozada; desarróllela más.

## 2. Calidad de la explicación teórica (22 / 25)
**Lo que hizo bien:**
- Define peor caso, mejor caso y caso promedio, fija el tamaño `n` y justifica que usaría el peor caso por la ventana estricta.
- La predicción por escenario quedó escrita antes del experimento.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el árbol de recursión hasta `Θ(n log n)`.
- Presenta la tabla de complejidades por caso.

**Lo que puede mejorar:**
- El cálculo línea a línea de insertion sort en su imagen corresponde a otra versión del código (con la condición dentro del `while`), no a la que entregó, y solo desarrolla el peor caso. Hágalo sobre el código final y muestre también el mejor caso.
- En el árbol de recursión falta mostrar el número de niveles y el costo total con la misma claridad que el resto del desarrollo.

## 3. Corrección de la implementación (18 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien los tres escenarios, no cambian la lista original y cuentan comparaciones entre elementos (9 en el mejor caso con 10 datos, como debe ser).
- No usa `sorted()` ni `list.sort()`; la mezcla de merge sort es propia.
- Los generadores producen listas del tamaño pedido, sin repetidos y con semilla reproducible.

**Lo que puede mejorar:**
- En `parte4_complejidad.py` el parámetro `algoritmo` no tiene *type hint*.
- En `generar_inverso` falta la línea en blanco antes de `Returns:` en el *docstring*.
- Hay una línea de más de 100 caracteres en `parte3_casos.py`.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas tienen título, ejes rotulados y leyenda. Las cifras del informe coinciden con ellas: en `parte4_tiempo.png` insertion sort llega a cerca de 1 segundo en n = 6400, y en `parte3_tiempo.png` el escenario inverso llega a cerca de 2 segundos.
- Identifica correctamente el peor caso (C), el mejor (B) y el más cercano al promedio (A), y lo contrasta con su predicción.
- El concepto técnico recomienda merge sort, responde a la propuesta del servidor con un dato medido, extrapola a 1.200.000 registros (unas 9,8 horas contra unos 4,5 segundos) y lo declara como estimación.

**Lo que puede mejorar:**
- Sobre los tamaños pequeños, diga con más claridad por qué las dos curvas casi no se distinguen y cuándo empieza a notarse la diferencia.
- La afirmación de que la memoria extra de merge sort es "minúscula" no está respaldada por ninguna medición ni cálculo; estime cuánta memoria usaría.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada y los archivos pedidos.
- El informe está ordenado por partes, las gráficas se ven y cada parte enlaza su código.
- Incluye instrucciones de reproducción y tiene muchos commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Los algoritmos ordenan correctamente, el experimento de la Parte 4 corre sin errores y genera la gráfica.

## Para el próximo laboratorio
- Convierta siempre el tiempo medido en una cifra concreta (energía, costo o memoria) cuando el informe lo pida.
- Haga el análisis línea a línea sobre el código exacto que entrega, cubriendo mejor, peor y promedio.
- Revise *type hints*, *docstrings* y longitud de líneas antes de publicar.
- Apoye cada afirmación sobre recursos, como la memoria, en un cálculo o una medición.
