"""Experimento de la Parte 4: Comparación de rendimiento entre Insertion Sort y Merge Sort."""

import time

import matplotlib.pyplot as plt
from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

REPETICIONES = 5


def medir_tiempo(algoritmo, datos: list[int]) -> float:
    """Ejecuta un algoritmo cinco veces y retorna su tiempo promedio.

    Args:
        algoritmo: funcion de ordenamiento que recibe una lista de enteros.
        datos: lote que se ordena en cada repeticion.

    Returns:
        Tiempo promedio de ejecucion en segundos.
    """
    tiempos: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        tiempos.append(time.perf_counter() - inicio)
    return sum(tiempos) / REPETICIONES


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

    print(f"{'n':<6} | {'Algoritmo':<18} | {'Comparaciones':<15} | Tiempo promedio (s)")
    print("-" * 60)

    for n in tamanos:
        datos = generar_aleatorio(n)

        _, comp_ins = insertion_sort(datos)
        tiempo_ins = medir_tiempo(insertion_sort, datos)

        resultados["Insertion Sort"]["comparaciones"].append(comp_ins)
        resultados["Insertion Sort"]["tiempos"].append(tiempo_ins)

        print(
            f"{n:<6} | {'Insertion Sort':<18} | {comp_ins:<15,} | {tiempo_ins:>12.6f}"
        )

        _, comp_merge = merge_sort(datos)
        tiempo_merge = medir_tiempo(merge_sort, datos)

        resultados["Merge Sort"]["comparaciones"].append(comp_merge)
        resultados["Merge Sort"]["tiempos"].append(tiempo_merge)

        print(
            f"{n:<6} | {'Merge Sort':<18} | {comp_merge:<15,} | {tiempo_merge:>12.6f}"
        )
        print("-" * 60)

    generar_graficas(tamanos, resultados)


def generar_graficas(
    tamanos: list[int], resultados: dict[str, dict[str, list[float]]]
) -> None:
    """Genera y guarda la gráfica comparativa de Tiempo de Ejecución vs Tamaño de Entrada.

    Args:
        tamanos: Lista de tamaños de entrada.
        resultados: Diccionario con los resultados del experimento.
    """
    plt.figure(figsize=(9, 5))
    for algoritmo, metricas in resultados.items():
        plt.plot(tamanos, metricas["tiempos"], label=algoritmo)

    plt.title("Parte 4 — Tiempo de Ejecución vs. Tamaño de Entrada (Escenario A)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo promedio (segundos, 5 repeticiones)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("graficas/parte4_tiempo.png", dpi=150)
    plt.close()

    print(
        "\nExperimento completado con éxito. Gráfica guardada en 'graficas/parte4_tiempo.png'."
    )


if __name__ == "__main__":
    ejecutar_experimento()
