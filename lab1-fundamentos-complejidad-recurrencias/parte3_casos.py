"""Experimento de la Parte 3: Evaluación de tiempos y comparaciones de Insertion Sort."""

import time
import matplotlib.pyplot as plt
from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

def ejecutar_experimento() -> None:
    """Ejecuta las pruebas de rendimiento de Insertion Sort en los 3 escenarios.
    
        Cronometra únicamente el tiempo de ejecución del algoritmo y registra el
        número total de comparaciones de elementos para cada tamaño de entrada
        definido en tamanos
        """

    tamanos = [100, 200, 400, 800, 1600, 3200, 6400]
    
    resultados: dict[str, dict[str, list[float]]] = {
        "A (Aleatorio)": {"comparaciones": [], "tiempos": []},
        "B (Casi ordenado)": {"comparaciones": [], "tiempos": []},
        "C (Inverso)": {"comparaciones": [], "tiempos": []},
    }

    #Encabezado de la tabla de resultados
    print(f"{'n':<6} | {'Escenario':<18} | {'Comparaciones':<15} | {'Tiempo (s)':<12}")
    print("-" * 60)

    for n in tamanos:
        
        lotes: dict[str, list[int]] = {
            "A (Aleatorio)": generar_aleatorio(n),
            "B (Casi ordenado)": generar_casi_ordenado(n),
            "C (Inverso)": generar_inverso(n),
        }

        for escenario, datos in lotes.items():
            inicio = time.perf_counter()
            lista_ordenada, comparaciones = insertion_sort(datos)
            fin = time.perf_counter()

            tiempo_ejecucion = fin - inicio

            resultados[escenario]["comparaciones"].append(comparaciones)
            resultados[escenario]["tiempos"].append(tiempo_ejecucion)

            print(f"{n:<6} | {escenario:<18} | {comparaciones:<15,} | {tiempo_ejecucion:<12.6f}")
        print("-" * 60)

    generar_graficas(tamanos, resultados)

def generar_graficas(tamanos: list[int], resultados: dict[str, dict[str, list[float]]]) -> None:
    """Genera y guarda las gráficas de Comparaciones vs Tamaño de Entrada y Tiempo vs Tamaño de Entrada.
    
    Args:
        tamanos: Lista de tamaños de entrada.
        resultados: Diccionario con los resultados del experimento.
    """

    plt.figure()
    for escenario, metricas in resultados.items():
        plt.plot(tamanos, metricas["comparaciones"], label=escenario)
    
    plt.title("Parte 3 — Comparaciones vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de Comparaciones")
    plt.grid(True)
    plt.legend()
    plt.savefig("graficas/parte3_comparaciones.png")
    plt.close()


    plt.figure()
    for escenario, metricas in resultados.items():
        plt.plot(tamanos, metricas["tiempos"], label=escenario)
    
    plt.title("Parte 3 — Tiempo de Ejecución vs. Tamaño de Entrada (Insertion Sort)")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de Ejecución (segundos)")
    plt.grid(True)
    plt.legend()
    plt.savefig("graficas/parte3_tiempo.png")
    plt.close()

    print("\nExperimento completado con éxito. Gráficas guardadas en 'graficas/'.")


if __name__ == "__main__":
    ejecutar_experimento()