# Retroalimentación — Laboratorio 02: Dividir y vencer

**Estudiante:** Carla Giraldo Camacho · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-30 23:59 · **Versión revisada:** commit `6687e8b`

Excelente trabajo: un laboratorio completo, bien verificado y con un análisis apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 20 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 25 / 25 |
| Calidad del análisis de las gráficas | 25 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **100 / 100** |
| **Nota (0–5)** | **5.00** |

## 1. Corrección conceptual (20 / 20)
**Lo que hizo bien:**
- Identifica con sus datos el tamaño desde el cual divide y vencerás empieza a ganar (n = 50) y aclara que la diferencia allí es pequeña y puede variar entre equipos.
- Explica bien por qué buscar solo el máximo no mejora al dividir: combinar cuesta un tiempo constante, la recurrencia sigue siendo lineal y solo se añaden llamadas.
- Recomienda un algoritmo, estima el tiempo para 1.000.000 de registros sin usar una regla de tres lineal y declara que es una estimación.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Plantea la recurrencia explicando de dónde sale cada término (dos mitades y un recorrido para el caso cruzado).
- Resuelve con el método maestro y verifica la condición del caso 2 comparando `f(n)` con `n^(log_b a)`.
- Justifica que la fuerza bruta es `Θ(n²)` contando las iteraciones.

## 3. Corrección de la implementación (25 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en la serie de ocho días, un elemento, todos negativos, todos positivos y un caso cruzado.
- `subarreglo_maximo` resuelve los tres casos sin llamar a la fuerza bruta y no modifica la lista recibida.
- Las pruebas comparan 25 listas aleatorias entre ambas soluciones, por suma y no por índices.
- Todas las funciones del código tienen *type hints*, *docstrings* con `Args` y `Returns`, y dos líneas en blanco entre funciones.

## 4. Calidad del análisis de las gráficas (25 / 25)
**Lo que hizo bien:**
- La gráfica `tiempo_vs_n.png` tiene ambas curvas en los mismos ejes, título, ejes rotulados y leyenda, con ocho tamaños.
- Lo que dice el informe coincide con la gráfica publicada: la fuerza bruta llega a cerca de 0,37 s en n = 4000 y divide y vencerás queda casi pegada al eje.
- Calcula los factores de crecimiento al duplicar `n` en tres pares de tamaños y los contrasta con 4 para `Θ(n²)` y con los valores de `n log n`.
- Mide con la misma lista para ambos algoritmos, semilla fija y 30 repeticiones, y comprueba dentro del experimento que las sumas coinciden.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- La carpeta `lab2-divide-y-vencer/` tiene la estructura pedida: `README.md`, `subarreglo.py`, `pruebas.py`, `medicion.py` y `graficas/tiempo_vs_n.png`.
- El informe sigue el orden pedido, trae su nombre e instrucciones de reproducción, enlaza el código de cada parte y la gráfica se ve con ruta relativa.
- Tiene varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, la medición corre completa y regenera la gráfica sin errores.
