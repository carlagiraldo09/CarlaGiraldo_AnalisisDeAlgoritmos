"""Pruebas de la lista enlazada y la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 20261028
COLECCIONES_ALEATORIAS = 50


def probar_casos_basicos() -> None:
    """Verifica busquedas exitosas e infructuosas."""
    lista = ListaEnlazada()
    tabla = TablaHash(11)

    assert lista.buscar(1000000010) is None
    assert tabla.buscar(1000000010) is None

    lista.insertar(1000000010, "en bodega")
    tabla.insertar(1000000010, "en bodega")

    assert lista.buscar(1000000010) == "en bodega"
    assert tabla.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000099) is None
    assert tabla.buscar(1000000099) is None
    assert lista.tamano == 1
    assert tabla.tamano == 1


def probar_colision_forzada() -> None:
    """Verifica tres claves que colisionan en la casilla 3."""
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")

    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.casillas[3].tamano == 3
    assert tabla.factor_carga() == 3 / 7


def generar_inexistente(
    existentes: set[int], generador: random.Random
) -> int:
    """Genera una guia que no pertenece a la coleccion.

    Args:
        existentes: Guias ya almacenadas.
        generador: Generador aleatorio reproducible.

    Returns:
        Una guia de diez digitos que no esta en la coleccion.
    """
    guia = generador.randint(10**9, 10**10 - 1)
    while guia in existentes:
        guia = generador.randint(10**9, 10**10 - 1)
    return guia


def probar_colecciones_aleatorias() -> None:
    """Compara ambas estructuras en cincuenta colecciones."""
    generador = random.Random(SEMILLA)
    estados = ["en bodega", "en reparto", "entregado"]
    tamanos_tabla = [7, 11, 23, 47]

    for _ in range(COLECCIONES_ALEATORIAS):
        cantidad = generador.randint(1, 100)
        guias = generador.sample(range(10**9, 10**10), cantidad)
        lista = ListaEnlazada()
        tabla = TablaHash(generador.choice(tamanos_tabla))
        esperados: dict[int, str] = {}

        for indice, guia in enumerate(guias):
            estado = estados[indice % len(estados)]
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
            esperados[guia] = estado

        for guia in guias:
            assert lista.buscar(guia) == esperados[guia]
            assert tabla.buscar(guia) == esperados[guia]

        conjunto_guias = set(guias)
        for _ in range(10):
            inexistente = generar_inexistente(conjunto_guias, generador)
            assert lista.buscar(inexistente) is None
            assert tabla.buscar(inexistente) is None

        assert lista.tamano == cantidad
        assert tabla.tamano == cantidad
        assert tabla.factor_carga() == cantidad / tabla.m


def ejecutar_pruebas() -> None:
    """Ejecuta todos los casos de prueba."""
    probar_casos_basicos()
    probar_colision_forzada()
    probar_colecciones_aleatorias()
    print("Todas las pruebas pasaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
