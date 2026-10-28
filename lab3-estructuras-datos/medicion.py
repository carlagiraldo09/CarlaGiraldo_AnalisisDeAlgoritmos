"""Mediciones de busqueda en lista enlazada y tabla hash."""

from pathlib import Path
import random
import time
from typing import Callable

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 20261028
BUSQUEDAS_POR_LOTE = 200
REPETICIONES = 20
TAMANOS_Y_CASILLAS = [
    (100, 53),
    (500, 251),
    (1000, 503),
    (5000, 2503),
    (20000, 10007),
    (50000, 25013),
]
N_FACTOR_CARGA = 20000
CASILLAS_POR_ALFA = [80021, 40009, 20011, 10007, 5003, 2003]
CARPETA_GRAFICAS = Path(__file__).parent / "graficas"


def generar_guias(cantidad: int, semilla: int) -> list[int]:
    """Genera guias distintas de diez digitos.

    Args:
        cantidad: Numero de guias que se generan.
        semilla: Semilla para reproducir los datos.

    Returns:
        Una lista de guias distintas.
    """
    generador = random.Random(semilla)
    return generador.sample(range(10**9, 10**10), cantidad)


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: Guias almacenadas en las estructuras.
        cantidad: Cuantas guias inexistentes se generan.
        semilla: Semilla del generador para reproducir la medicion.

    Returns:
        Una lista con guias que no pertenecen a existentes.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def construir_estructuras(
    guias: list[int], m: int
) -> tuple[ListaEnlazada, TablaHash]:
    """Construye ambas estructuras con las mismas guias.

    Args:
        guias: Guias que se almacenan.
        m: Numero de casillas de la tabla.

    Returns:
        La lista enlazada y la tabla hash construidas.
    """
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for guia in guias:
        lista.insertar(guia, "en bodega")
        tabla.insertar(guia, "en bodega")
    return lista, tabla


def medir_busquedas(
    buscar: Callable[[int], str | None], guias: list[int]
) -> float:
    """Calcula el tiempo medio de una busqueda infructuosa.

    Args:
        buscar: Metodo de busqueda que se mide.
        guias: Guias inexistentes que se consultan.

    Returns:
        El tiempo medio por busqueda, en segundos.
    """
    tiempo_total = 0.0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in guias:
            buscar(guia)
        tiempo_total += time.perf_counter() - inicio
    cantidad_total = REPETICIONES * len(guias)
    return tiempo_total / cantidad_total


def verificar_muestra(
    lista: ListaEnlazada, tabla: TablaHash, guias: list[int]
) -> None:
    """Comprueba que ambas estructuras coincidan en una muestra.

    Args:
        lista: Lista enlazada construida.
        tabla: Tabla hash construida.
        guias: Guias existentes que se verifican.
    """
    for guia in guias[:20]:
        assert lista.buscar(guia) == "en bodega"
        assert tabla.buscar(guia) == "en bodega"
        assert lista.buscar(guia) == tabla.buscar(guia)


def experimento_lista_vs_tabla(
) -> list[tuple[int, int, float, float, float]]:
    """Mide la lista y la tabla al aumentar el numero de guias.

    Returns:
        Tuplas con n, m, alfa y los dos tiempos en microsegundos.
    """
    resultados: list[tuple[int, int, float, float, float]] = []
    for n, m in TAMANOS_Y_CASILLAS:
        guias = generar_guias(n, SEMILLA + n)
        conjunto = set(guias)
        inexistentes = generar_guias_inexistentes(
            conjunto, BUSQUEDAS_POR_LOTE, SEMILLA + n + 1
        )
        lista, tabla = construir_estructuras(guias, m)
        verificar_muestra(lista, tabla, guias)

        tiempo_lista = medir_busquedas(lista.buscar, inexistentes) * 10**6
        tiempo_tabla = medir_busquedas(tabla.buscar, inexistentes) * 10**6
        resultados.append(
            (n, m, tabla.factor_carga(), tiempo_lista, tiempo_tabla)
        )
    return resultados


def experimento_factor_carga() -> list[tuple[float, int, float]]:
    """Mide la tabla con diferentes factores de carga.

    Returns:
        Tuplas con alfa, m y tiempo medio en microsegundos.
    """
    guias = generar_guias(N_FACTOR_CARGA, SEMILLA)
    conjunto = set(guias)
    inexistentes = generar_guias_inexistentes(
        conjunto, BUSQUEDAS_POR_LOTE, SEMILLA + 1
    )
    resultados: list[tuple[float, int, float]] = []

    for m in CASILLAS_POR_ALFA:
        _, tabla = construir_estructuras(guias, m)
        for guia in guias[:20]:
            assert tabla.buscar(guia) == "en bodega"
        tiempo = medir_busquedas(tabla.buscar, inexistentes) * 10**6
        resultados.append((tabla.factor_carga(), m, tiempo))
    return resultados


def generar_grafica_lista_tabla(
    resultados: list[tuple[int, int, float, float, float]],
) -> None:
    """Guarda la grafica que compara lista y tabla.

    Args:
        resultados: Resultados del primer experimento.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    tamanos = [fila[0] for fila in resultados]
    tiempos_lista = [fila[3] for fila in resultados]
    tiempos_tabla = [fila[4] for fila in resultados]

    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.plot(tamanos, tiempos_lista, "o-", label="Lista enlazada")
    plt.plot(tamanos, tiempos_tabla, "o-", label="Tabla hash")
    plt.title("Busqueda infructuosa: lista enlazada frente a tabla hash")
    plt.xlabel("Numero de guias, n (elementos)")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def generar_grafica_factor_carga(
    resultados: list[tuple[float, int, float]],
) -> None:
    """Guarda la grafica del tiempo frente al factor de carga.

    Args:
        resultados: Resultados del segundo experimento.
    """
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    alfas = [fila[0] for fila in resultados]
    tiempos = [fila[2] for fila in resultados]

    CARPETA_GRAFICAS.mkdir(exist_ok=True)
    plt.figure(figsize=(9, 5))
    plt.plot(alfas, tiempos, "o-", label="Tabla hash")
    plt.title("Efecto del factor de carga en la busqueda infructuosa")
    plt.xlabel("Factor de carga, alfa = n / m")
    plt.ylabel("Tiempo medio por busqueda (microsegundos)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.savefig(CARPETA_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()


def mostrar_resultados(
    resultados_a: list[tuple[int, int, float, float, float]],
    resultados_b: list[tuple[float, int, float]],
) -> None:
    """Imprime las mediciones de los dos experimentos.

    Args:
        resultados_a: Resultados de lista frente a tabla.
        resultados_b: Resultados del factor de carga.
    """
    print("Experimento A")
    print("n | m | alfa | lista (us) | tabla (us)")
    for fila in resultados_a:
        print(
            f"{fila[0]} | {fila[1]} | {fila[2]:.4f} | "
            f"{fila[3]:.4f} | {fila[4]:.4f}"
        )

    print("\nExperimento B")
    print("alfa | m | tabla (us)")
    for fila in resultados_b:
        print(f"{fila[0]:.4f} | {fila[1]} | {fila[2]:.4f}")


def ejecutar_experimentos() -> None:
    """Ejecuta las mediciones y genera las dos graficas."""
    resultados_a = experimento_lista_vs_tabla()
    resultados_b = experimento_factor_carga()
    mostrar_resultados(resultados_a, resultados_b)
    generar_grafica_lista_tabla(resultados_a)
    generar_grafica_factor_carga(resultados_b)
    print(f"\nGraficas guardadas en {CARPETA_GRAFICAS}")


if __name__ == "__main__":
    ejecutar_experimentos()
