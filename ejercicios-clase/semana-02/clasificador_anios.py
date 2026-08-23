"""Clasificador de años bisiestos.
 
Complete las funciones siguiendo la especificación de cada docstring.
"""
 
 
def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto.
 
    Un año es bisiesto si es divisible por 4, excepto los años
    divisibles por 100 que no lo sean también por 400.
 
    Args:
        anio: año a evaluar (número entero).
 
    Returns:
        True si el año es bisiesto, False en caso contrario.
    """
    if anio % 4 == 0:
        if anio % 100 == 0 and anio % 400 == 0:
            return True
        elif anio % 100 == 0 and anio % 400 != 0:
            return False
        else:
            return True
    else:
        return False
 
 
def leer_anios() -> list[int]:
    """Solicita al usuario una lista de años separados por comas.
 
    Debe reintentar mientras la entrada no se pueda convertir a enteros
    (use try / except para capturar entradas inválidas).
 
    Returns:
        Lista de años como enteros.
    """
    while True:
        try:
            entrada = input("Ingrese una lista de años separados por comas: ")
            anios = [int(item.strip()) for item in entrada.split(",") if item.strip()]
            
            if not anios:
                print("Por favor, ingrese al menos un año.\n")
                continue 
            return anios
        except ValueError:
            print("Por favor, ingrese solo números enteros separados por comas.\n")


def main() -> None:
    """Punto de entrada del script."""
    lista_anios = leer_anios()
    anios_bisiestos = [anio for anio in lista_anios if es_bisiesto(anio)]
    print(f"\nLos años bisiestos en la lista son: {anios_bisiestos}")
    print(f"Total de años bisiestos: {len(anios_bisiestos)}")
 
 
if __name__ == "__main__":
    main()