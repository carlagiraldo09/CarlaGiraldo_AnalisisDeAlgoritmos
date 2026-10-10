# Laboratorio evaluativo 02 — Dividir y vencer

#### Estudiante: Carla Juliana Giraldo Camacho

---

### Instrucciones para reproducir el experimento

Desde la raíz del repositorio, cree y active el entorno virtual e instale las dependencias. Después ingrese a la carpeta del laboratorio.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd lab2-divide-y-vencer
```

En Windows, la activación es `venv\Scripts\activate`. Para comprobar las soluciones ejecute:

```bash
python pruebas.py
```

Para repetir las mediciones y regenerar la gráfica ejecute:

```bash
python medicion.py
```

---

## Parte 1 — Implementar y verificar

[Ver `subarreglo.py`](subarreglo.py) · [Ver `pruebas.py`](pruebas.py)

Implementé dos formas de buscar la mejor racha de variaciones consecutivas. La primera conserva una suma acumulada para cada día inicial y revisa todos los finales posibles. La segunda divide el rango en dos mitades, resuelve cada mitad y compara esos resultados con la mejor racha que atraviesa el punto medio.

Las pruebas cubren la serie propuesta de ocho días, una lista de un elemento, listas solo negativas y solo positivas, una racha óptima que cruza el medio y 25 listas aleatorias. En las listas aleatorias se compara la suma devuelta por ambas soluciones; no se exigen índices iguales porque pueden existir empates válidos.

## Parte 2 — Medir y graficar

[Ver `medicion.py`](medicion.py)

La gráfica se obtuvo con listas reproducibles de enteros entre -100 y 100, usando la semilla fija `20261003`. Para cada tamaño usé exactamente la misma lista en ambas funciones, comprobé que devolvieran la misma suma y promedié cinco ejecuciones. El cronómetro rodea únicamente la llamada del algoritmo; la generación de datos queda fuera de la medición.

![Tiempo de ejecución frente al tamaño de entrada](graficas/tiempo_vs_n.png)

## Parte 3 — Análisis

### 1. Recurrencia y complejidad

Para `subarreglo_maximo`, una llamada de tamaño `n` crea dos subproblemas de aproximadamente `n/2`: uno para la mitad izquierda y otro para la derecha. Además, calcula el caso que atraviesa el punto medio. Ese cálculo recorre una vez la mitad izquierda hacia atrás y una vez la derecha hacia adelante; entre los dos recorridos cuesta Θ(n). Por tanto, la recurrencia es `T(n) = 2T(n/2) + Θ(n)`, con caso base de un elemento.

En el método maestro, `a = 2` y `b = 2`, así que `n^(log_b a) = n^(log_2 2) = n`. Como el término de combinación también es Θ(n), tiene el mismo orden que ese valor. Corresponde al caso 2 y el resultado es Θ(n log n).

La fuerza bruta acumulada no vuelve a sumar desde cero cada tramo. Para cada índice inicial recorre los finales posibles y actualiza una suma, lo que forma aproximadamente `n(n + 1) / 2` iteraciones. Esa cantidad es Θ(n²).

### 2. Lo medido frente a lo esperado

Los datos de esta ejecución se muestran en la tabla siguiente. Los factores se calculan al pasar de `n = 2000` a `n = 4000`. La curva de fuerza bruta se vuelve mucho más inclinada porque al duplicar `n` se revisan cerca de cuatro veces más pares. La de divide y vencerás también crece, pero con una pendiente menor: duplicar `n` duplica el trabajo principal y añade solo un nivel logarítmico.

| Algoritmo | Tiempo en 2000 | Tiempo en 4000 | Factor al duplicar |
|---|---:|---:|---:|
| Fuerza bruta | 0,0927257 s | 0,3655947 s | 3,94 |
| Divide y vencerás | 0,0027799 s | 0,0057898 s | 2,08 |

El factor esperado para fuerza bruta es aproximadamente 4, por lo que el 3,94 medido coincide muy bien con Θ(n²). Para divide y vencerás, el factor esperado es `(4000 log₂ 4000) / (2000 log₂ 2000)`, cerca de 2,18. El valor observado, 2,08, está próximo: pequeñas diferencias son normales por el temporizador y la carga del equipo. La forma de la gráfica respalda esa comparación.

### 3. Tamaños pequeños

En listas pequeñas las dos curvas quedan cercanas porque la recursión tiene costos fijos: crear llamadas, calcular el medio y construir sus retornos. La ventaja de divide y vencerás aparece cuando el trabajo cuadrático de fuerza bruta deja de ser pequeño frente a esos costos. El punto preciso puede variar según el computador y la versión de Python; por eso el resultado se interpreta desde los tiempos de esta ejecución y no como una constante universal.

### 4. ¿Cuándo conviene dividir?

Para hallar solo el máximo de un arreglo no conviene dividir si ya existe un recorrido simple. La versión recursiva tendría `T(n) = 2T(n/2) + Θ(1)`: resuelve dos mitades y compara sus dos máximos con costo constante. Por método maestro es Θ(n), igual que recorrer una vez el arreglo. No reduce el orden de crecimiento y añade llamadas recursivas, por lo que en este caso la pasada iterativa suele ser preferible. Dividir ayuda cuando la combinación evita una alternativa peor, como sucede aquí al tratar explícitamente el tramo cruzado.

### 5. Concepto para la gerente

Recomiendo divide y vencerás para las series grandes de la cooperativa. Conserva la misma respuesta que fuerza bruta, pero su crecimiento es Θ(n log n), mientras que fuerza bruta crece como Θ(n²). Para una serie de 1.000.000 de registros, la estimación parte de un punto medido, no de una regla de tres lineal. Desde el tiempo de `n = 4000`, fuerza bruta se escala por `(1.000.000 / 4000)²`: `0,3655947 × 62.500` da cerca de 22.850 s, o 6,35 horas. Divide y vencerás se escala por `(1.000.000 log₂ 1.000.000) / (4000 log₂ 4000)`; el factor es 416,43 y `0,0057898 × 416,43` estima unos 2,41 s. Son estimaciones: el hardware, la memoria y el intérprete pueden modificar el tiempo real, pero la diferencia de crecimiento explica por qué conviene la solución recursiva para cientos de miles o millones de registros.
