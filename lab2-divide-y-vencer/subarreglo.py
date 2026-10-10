"""Soluciones de fuerza bruta y divide y vencerás para subarreglo máximo."""


def subarreglo_fuerza_bruta(valores: list[float]) -> tuple[int, int, float]:
    """Encuentra la mejor racha probando todos los pares de días.

    Args:
        valores: Variación diaria de caja, con al menos un elemento.

    Returns:
        Una tupla con el índice inicial, el índice final y la suma máxima.
    """
    mejor_inicio = 0
    mejor_fin = 0
    mejor_suma = float("-inf")

    for inicio in range(len(valores)):
        suma_actual = 0.0
        for fin in range(inicio, len(valores)):
            suma_actual += valores[fin]
            if suma_actual > mejor_suma:
                mejor_inicio = inicio
                mejor_fin = fin
                mejor_suma = suma_actual

    return mejor_inicio, mejor_fin, mejor_suma


def suma_cruzada(
    valores: list[float], inicio: int, medio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha que cruza el punto medio.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango considerado, inclusive.
        medio: Índice final de la mitad izquierda.
        fin: Índice final del rango considerado, inclusive.

    Returns:
        Una tupla con el inicio, el fin y la suma de la mejor racha cruzada.
    """
    suma_actual = 0.0
    mejor_suma_izquierda = float("-inf")
    mejor_inicio = medio
    for indice in range(medio, inicio - 1, -1):
        suma_actual += valores[indice]
        if suma_actual > mejor_suma_izquierda:
            mejor_suma_izquierda = suma_actual
            mejor_inicio = indice

    suma_actual = 0.0
    mejor_suma_derecha = float("-inf")
    mejor_fin = medio + 1
    for indice in range(medio + 1, fin + 1):
        suma_actual += valores[indice]
        if suma_actual > mejor_suma_derecha:
            mejor_suma_derecha = suma_actual
            mejor_fin = indice

    return mejor_inicio, mejor_fin, mejor_suma_izquierda + mejor_suma_derecha


def subarreglo_maximo(
    valores: list[float], inicio: int, fin: int
) -> tuple[int, int, float]:
    """Encuentra la mejor racha con el esquema divide y vencerás.

    Args:
        valores: Variación diaria de caja.
        inicio: Índice inicial del rango a considerar, inclusive.
        fin: Índice final del rango a considerar, inclusive.

    Returns:
        Una tupla con el inicio, el fin y la suma máxima en el rango indicado.
    """
    if inicio == fin:
        return inicio, fin, float(valores[inicio])

    medio = (inicio + fin) // 2
    izquierda = subarreglo_maximo(valores, inicio, medio)
    derecha = subarreglo_maximo(valores, medio + 1, fin)
    cruzada = suma_cruzada(valores, inicio, medio, fin)

    if izquierda[2] >= derecha[2] and izquierda[2] >= cruzada[2]:
        return izquierda
    if derecha[2] >= izquierda[2] and derecha[2] >= cruzada[2]:
        return derecha
    return cruzada
