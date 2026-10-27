"""Experimento de rendimiento para subarreglo máximo."""

from pathlib import Path
import random
import time
from typing import Callable

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

REPETICIONES = 30
SEMILLA = 20261003
TAMANOS = [10, 50, 100, 250, 500, 1000, 2000, 4000]
RUTA_GRAFICA = Path(__file__).parent / "graficas" / "tiempo_vs_n.png"


def medir_tiempo(
    algoritmo: Callable[[list[float]], tuple[int, int, float]],
    valores: list[float],
) -> float:
    """Mide el tiempo promedio de una función sobre una misma lista.

    Args:
        algoritmo: Función que resuelve el subarreglo máximo.
        valores: Lista de variaciones sobre la cual se mide la función.

    Returns:
        Tiempo promedio de las ejecuciones, en segundos.
    """
    tiempos: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(valores)
        tiempos.append(time.perf_counter() - inicio)
    return sum(tiempos) / len(tiempos)


def resolver_divide_y_venceras(
    valores: list[float],
) -> tuple[int, int, float]:
    """Adapta la firma recursiva para usarla en la medición.

    Args:
        valores: Lista no vacía de variaciones.

    Returns:
        La racha máxima de toda la lista.
    """
    return subarreglo_maximo(valores, 0, len(valores) - 1)


def generar_grafica(
    tamanos: list[int],
    tiempos_fuerza_bruta: list[float],
    tiempos_divide: list[float],
) -> None:
    """Guarda la gráfica comparativa de tiempos.

    Args:
        tamanos: Tamaños de las listas medidas.
        tiempos_fuerza_bruta: Tiempos promedio de fuerza bruta.
        tiempos_divide: Tiempos promedio de divide y vencerás.
    """
    RUTA_GRAFICA.parent.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_fuerza_bruta, "o-", label="Fuerza bruta Θ(n²)")
    plt.plot(
        tamanos,
        tiempos_divide,
        "o-",
        label="Divide y vencerás Θ(n log n)",
    )
    plt.title("Subarreglo máximo: tiempo de ejecución vs. tamaño")
    plt.xlabel("Tamaño de entrada, n (elementos)")
    plt.ylabel("Tiempo promedio (segundos; 30 repeticiones)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(RUTA_GRAFICA, dpi=150)
    plt.close()


def mostrar_factores(
    tamanos: list[int],
    tiempos_fuerza_bruta: list[float],
    tiempos_divide: list[float],
) -> None:
    """Muestra el crecimiento entre pares consecutivos de mediciones.

    Args:
        tamanos: Tamaños de las listas medidas.
        tiempos_fuerza_bruta: Tiempos promedio de fuerza bruta.
        tiempos_divide: Tiempos promedio de divide y vencerás.
    """
    print("\nFactores entre tamaños consecutivos")
    print(f"{'Cambio de n':>15} | {'Fuerza bruta':>14} | {'Divide':>10}")
    print("-" * 47)
    for indice in range(1, len(tamanos)):
        cambio = f"{tamanos[indice - 1]} -> {tamanos[indice]}"
        factor_bruta = tiempos_fuerza_bruta[indice] / tiempos_fuerza_bruta[
            indice - 1
        ]
        factor_divide = tiempos_divide[indice] / tiempos_divide[indice - 1]
        print(f"{cambio:>15} | {factor_bruta:>14.2f} | {factor_divide:>10.2f}")


def ejecutar_experimento() -> None:
    """Mide los algoritmos, comprueba sus resultados y crea la gráfica."""
    generador = random.Random(SEMILLA)
    tiempos_fuerza_bruta: list[float] = []
    tiempos_divide: list[float] = []

    print(f"{'n':>6} | {'Fuerza bruta (s)':>18} | {'Divide y vencerás (s)':>24}")
    print("-" * 58)
    for tamano in TAMANOS:
        valores = [generador.randint(-100, 100) for _ in range(tamano)]
        resultado_fuerza_bruta = subarreglo_fuerza_bruta(valores)
        resultado_divide = resolver_divide_y_venceras(valores)
        assert resultado_fuerza_bruta[2] == resultado_divide[2]

        tiempo_fuerza_bruta = medir_tiempo(subarreglo_fuerza_bruta, valores)
        tiempo_divide = medir_tiempo(resolver_divide_y_venceras, valores)
        tiempos_fuerza_bruta.append(tiempo_fuerza_bruta)
        tiempos_divide.append(tiempo_divide)
        print(
            f"{tamano:>6} | {tiempo_fuerza_bruta:>18.7f} | "
            f"{tiempo_divide:>24.7f}"
        )

    mostrar_factores(TAMANOS, tiempos_fuerza_bruta, tiempos_divide)
    generar_grafica(
        tamanos=TAMANOS,
        tiempos_fuerza_bruta=tiempos_fuerza_bruta,
        tiempos_divide=tiempos_divide,
    )
    print(f"\nGráfica guardada en: {RUTA_GRAFICA}")


if __name__ == "__main__":
    ejecutar_experimento()
