"""Experimento de la Parte 4: Comparación de rendimiento entre Insertion Sort y Merge Sort."""

import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio


def ejecutar_experimento() -> None:
    """Ejecuta las pruebas de rendimiento comparativas sobre el Escenario A (Aleatorio).

    Cronometra únicamente el tiempo de ejecución de cada algoritmo y registra el
    número total de comparaciones para los tamaños de entrada definidos en tamanos.
    """
    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]

    resultados: dict[str, dict[str, list[float]]] = {
        "Insertion Sort": {"comparaciones": [], "tiempos": []},
        "Merge Sort": {"comparaciones": [], "tiempos": []},
    }

    # Encabezado de la tabla de resultados
    print(f"{'n':<6} | {'Algoritmo':<18} | {'Comparaciones':<15} | {'Tiempo (s)':>12}")
    print("-" * 60)

    for n in tamanos:
        datos = generar_aleatorio(n)

        inicio = time.perf_counter()
        lista_ordenada_ins, comp_ins = insertion_sort(datos)
        fin = time.perf_counter()
        tiempo_ins = fin - inicio

        resultados["Insertion Sort"]["comparaciones"].append(comp_ins)
        resultados["Insertion Sort"]["tiempos"].append(tiempo_ins)

        print(f"{n:<6} | {'Insertion Sort':<18} | {comp_ins:<15,} | {tiempo_ins:>12.6f}")

        inicio = time.perf_counter()
        lista_ordenada_merge, comp_merge = merge_sort(datos)
        fin = time.perf_counter()
        tiempo_merge = fin - inicio

        resultados["Merge Sort"]["comparaciones"].append(comp_merge)
        resultados["Merge Sort"]["tiempos"].append(tiempo_merge)

        print(f"{n:<6} | {'Merge Sort':<18} | {comp_merge:<15,} | {tiempo_merge:>12.6f}")
        print("-" * 60)

    generar_graficas(tamanos, resultados)


