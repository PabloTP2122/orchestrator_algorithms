"""Algoritmo de para remover duplicados, dos versiones.
Versión de dos punteros y versión Pythinica.
"""


def remove_duplicates(logs: list[int]) -> int:
    """Recibe una lista de timestamps (logs) ordenada y elimina duplicados in-place.
    Utiliza el patrón Two Pointers (Reader/Writer).

    Args:
        logs: Lista ordenada de enteros.

    Returns:
        int: La nueva longitud efectiva de la lista sin duplicados.

    """
    # 1. Edge Case: Lista vacía
    if not logs:
        return 0
    # 2. Inicialización de punteros
    # 'left' es nuestro puntero de ESCRITURA (donde colocamos el valor único)
    left: int = 0

    # 3. Iteración
    # 'right' es nuestro puntero de LECTURA (explorador)
    for right in range(1, len(logs)):
        # Si encontramos un valor nuevo (diferente al último escrito)
        if logs[left] != logs[right]:
            left += 1
            logs[left] = logs[right]
    # Retornamos la longitud (índice + 1)
    return left + 1


def remove_duplicates_pythonic(logs: list[int]) -> int:
    """Recibe una lista de timestamps (logs) ordenada y elimina duplicados de forma
    'Pythonica'.

    Args:
        logs: Lista ordenada de enteros.

    Returns:
        int: La nueva longitud efectiva de la lista sin duplicados.


    """
    unique_list = list[int](set[int](logs))
    return len(unique_list)
