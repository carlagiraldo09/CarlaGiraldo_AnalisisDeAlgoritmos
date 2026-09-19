"""Generadores de lotes de registros para los escenarios de Tamiza."""
import random
 
def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio, para que el
            experimento sea reproducible.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, desordenada.
    """
    random.seed(semilla)
    aleatoria = [random.randint(0, 1000) for _ in range(n)]

    return aleatoria

def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, con el primer
        98% en el orden que el algoritmo produce y el 2% restante
        desordenado al final.
    """
    random.seed(semilla)
    datos = [random.randint(0, 1000) for _ in range(n)]

    n_ordenados = int(n * 0.98)

    # Profe, estoy usando sorted() ya que este no es el algortimo de Insertion Sort
    # a evaluar, sino que es un generador de datos para probarlo.
    parte_ordenada = sorted(datos[:n_ordenados], reverse=True)
    parte_desordenada = datos[n_ordenados:]

    casi_ordenada = parte_ordenada + parte_desordenada

    return casi_ordenada

def generar_inverso(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C).
 
    Args:
        n: cantidad de registros del lote.
        semilla: semilla del generador aleatorio.
 
    Returns:
        Lista de n indices de riesgo enteros distintos, en el orden
        inverso al que el algoritmo debe producir.
    """
    random.seed(semilla)
    datos = [random.randint(0, 1000) for _ in range(n)]
    inversa = sorted(datos)

    return inversa