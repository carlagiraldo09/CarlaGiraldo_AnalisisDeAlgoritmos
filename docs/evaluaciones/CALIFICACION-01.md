# Retroalimentación — Laboratorio 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Carla Giraldo Camacho · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-06 23:59 · **Versión revisada:** commit `7d295ef`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 19 / 25 |
| Corrección de la implementación | 14 / 20 |
| Calidad del análisis de las gráficas | 17 / 20 |
| Documentación y organización del informe | 8 / 10 |
| **Total** | **79 / 100** |
| **Nota (0–5)** | **3.95** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue entre que el resultado sea correcto y que llegue a tiempo, y nombra la restricción que se incumple: la ventana de cuatro horas.
- Explica que duplicar la velocidad del servidor no arregla el problema, porque el tiempo crece al cuadrado con los datos.
- Da un segundo ejemplo propio (cierre nocturno de un banco) con cantidad de datos y ventana de tiempo.
- En la Parte 2 relaciona el tiempo de ejecución con el gasto de energía todas las madrugadas, nombra quién asume el costo del error y trata la obligación de que el orden de la lista sea correcto.

**Lo que puede mejorar:**
- En el ejemplo del banco no queda claro qué algoritmo se usa ni cuánto tarda; dé una cifra aproximada de la ventana frente al tiempo real.
- En la parte ética, separe más los perjuicios concretos (por ejemplo, el paciente que no es llamado y el operador del centro de contacto) y diga quién asume el costo de cada uno.

## 2. Calidad de la explicación teórica (19 / 25)
**Lo que hizo bien:**
- Define los tres casos, justifica usar el peor caso para decidir si entra en producción y deja escrita la predicción antes del experimento.
- Plantea la recurrencia de merge sort con el árbol de recursión, con el costo por nivel, el número de niveles y la cota final O(n log n).
- Calcula insertion sort línea a línea y llega a la forma cuadrática.

**Lo que puede mejorar:**
- Falta la tabla con la complejidad de cada algoritmo en el mejor caso, el peor y el promedio.
- Al definir los casos, diga con más precisión sobre qué conjunto de entradas se toma el máximo, el mínimo y el promedio.
- El cálculo línea a línea de insertion sort solo desarrolla el peor caso, y su código de apoyo no coincide del todo con el que usted entregó.

## 3. Corrección de la implementación (14 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida y cuentan las comparaciones entre elementos. `merge_sort` tiene su propia mezcla recursiva.
- Los generadores usan semilla y las funciones tienen *type hints* y *docstrings*.

**Lo que puede mejorar:**
- Los generadores no producen índices distintos: usan números al azar que se repiten (en un lote de 1000 solo hay unos 640 valores distintos).
- `generar_inverso` cambió la firma pedida (agregó el parámetro `semilla`).
- Los generadores usan `sorted()`. Está justificado en un comentario porque no es el algoritmo evaluado, pero conviene evitarlo.
- Hay muchas faltas de estilo PEP 8: líneas con espacios sobrantes, falta de dos líneas en blanco entre funciones, líneas largas y archivos sin salto de línea final.

## 4. Calidad del análisis de las gráficas (17 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen y tienen título, ejes rotulados, leyenda y los escenarios en los mismos ejes.
- Identifica con evidencia el peor caso (inverso), el mejor (casi ordenado) y el promedio (aleatorio), y lo contrasta con su predicción.
- Concluye que merge sort conviene a partir de la gráfica y de sus mediciones, y lo relaciona con las complejidades.
- El concepto técnico recomienda un algoritmo, hace la extrapolación a 1.200.000 registros declarada como estimación y habla de memoria y estabilidad.

**Lo que puede mejorar:**
- Al responder sobre el servidor, cite explícitamente la gráfica de la que tomó el dato.
- Las curvas de tiempo salen de una sola medición; repetirla y promediar daría curvas más limpias.

## 5. Documentación y organización del informe (8 / 10)
**Lo que hizo bien:**
- Carpeta y archivos con los nombres pedidos, partes en orden, gráficas incrustadas que sí se ven y enlaces a cada código.
- Historial con muchos commits descriptivos.

**Lo que puede mejorar:**
- Las instrucciones activan el entorno virtual desde la carpeta del laboratorio, pero el entorno está en la raíz del repositorio; indique la ruta correcta.
- Los desarrollos de la Parte 4.1 están solo como fotos; funcionan, pero conviene acompañarlos de la tabla de complejidades en el informe.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores y generan las gráficas. Ambos algoritmos ordenan bien en mis pruebas con listas aleatorias, y el conteo de comparaciones es coherente.

## Para el próximo laboratorio
- Genere datos con valores distintos (por ejemplo, con `random.sample`) y respete las firmas pedidas.
- Corra una revisión de estilo PEP 8 antes de entregar y limpie espacios y líneas en blanco.
- Incluya siempre la tabla de mejor, peor y caso promedio, y desarrolle también el mejor caso del cálculo línea a línea.
- Cite la gráfica y el tamaño exacto de donde saca cada dato en sus recomendaciones.
- Revise que las instrucciones de reproducción funcionen desde la carpeta indicada.
