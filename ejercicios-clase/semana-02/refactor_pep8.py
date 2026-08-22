# def CalcularPromedio(Lista):
#     s=0
#     for x in Lista:
#      s=s+x
#     return s/len(Lista)
 
# l=[1,2,3,4,5]
# print(CalcularPromedio(l))

def calcular_promedio(numeros: list[float]) -> float:
    """Calcula el promedio de una lista de números

    Args:
        numeros (list[float]): Una lista de números de punto flotante

    Returns:
        float: El promedio de los números contenidos en la lista
    """
    suma = 0
    for numero in numeros:
        suma += numero

    return suma / len(numeros)


def main() -> None:
    """Función principal que ejecuta la lógica del código"""
    lista_numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(lista_numeros)
    print(promedio)


if __name__ == "__main__":
    main()