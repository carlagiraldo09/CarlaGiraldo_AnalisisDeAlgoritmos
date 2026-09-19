"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""

def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = 0
    arreglo = datos.copy()
    for i in range(1, len(arreglo)):
        clave = arreglo[i]
        j = i - 1
 
        while j >= 0:
            comparaciones += 1
            if clave > arreglo[j]:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            else:
                break
 
        arreglo[j + 1] = clave
    return arreglo, comparaciones

def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.
 
    No modifica la lista recibida: trabaja sobre una copia.
 
    Args:
        datos: lista de indices de riesgo a ordenar.
 
    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    arreglo = datos.copy()

    if len(arreglo) <= 1:
        return arreglo, 0
 
    mitad = len(arreglo) // 2
    izquierda, comparaciones_izquierda = merge_sort(arreglo[:mitad])
    derecha, comparaciones_derecha = merge_sort(arreglo[mitad:])

    lista_final, comp_mezcla = merge(izquierda, derecha)
    comparaciones_totales = comparaciones_izquierda + comparaciones_derecha + comp_mezcla

    return lista_final, comparaciones_totales
 
def merge(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ya ordenadas en una unica lista ordenada.
 
    Recorre ambas listas en paralelo, comparando siempre los
    elementos al frente y copiando el menor, hasta agotar una de
    las dos; despues copia lo que quede de la otra.
 
    Args:
        izquierda: lista ordenada de menor a mayor.
        derecha: lista ordenada de menor a mayor.
 
    Returns:
        Una lista ordenada con todos los elementos de izquierda y
        derecha.
    """
    comparaciones = 0

    resultado: list[int] = []
    i = j = 0
 
    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
 
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones