"""Pruebas de corrección de las soluciones de subarreglo máximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def suma_divide_y_venceras(valores: list[float]) -> float:
    """Obtiene solo la suma máxima con la solución recursiva.

    Args:
        valores: Lista no vacía de variaciones diarias.

    Returns:
        La suma máxima de una racha contigua.
    """
    return subarreglo_maximo(valores, 0, len(valores) - 1)[2]


def ejecutar_pruebas() -> None:
    """Verifica casos conocidos y coincidencia en listas aleatorias."""
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert suma_divide_y_venceras(serie) == 17

    un_elemento = [-7]
    assert subarreglo_fuerza_bruta(un_elemento)[2] == -7
    assert suma_divide_y_venceras(un_elemento) == -7

    todos_negativos = [-8, -3, -5, -10]
    assert subarreglo_fuerza_bruta(todos_negativos)[2] == -3
    assert suma_divide_y_venceras(todos_negativos) == -3

    todos_positivos = [2, 4, 1, 6]
    assert subarreglo_fuerza_bruta(todos_positivos)[2] == 13
    assert suma_divide_y_venceras(todos_positivos) == 13

    caso_cruzado = [-4, 7, 6, -2, 5, -8]
    assert subarreglo_fuerza_bruta(caso_cruzado)[2] == 16
    assert suma_divide_y_venceras(caso_cruzado) == 16

    generador = random.Random(20261003)
    for _ in range(25):
        longitud = generador.randint(1, 80)
        valores = [generador.randint(-100, 100) for _ in range(longitud)]
        suma_fuerza_bruta = subarreglo_fuerza_bruta(valores)[2]
        assert suma_divide_y_venceras(valores) == suma_fuerza_bruta

    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
