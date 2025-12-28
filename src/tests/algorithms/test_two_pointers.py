"""Tests para el algoritmo two_pointers."""

import timeit

from orchestrator.algorithms.two_pointers import (
    remove_duplicates,
    remove_duplicates_pythonic,
)


def test_remove_duplicates_basic() -> None:
    """Caso base: Lista con duplicados."""
    # Input: Logs ordenados con duplicados
    logs = [100, 100, 101, 102, 102, 102, 105]
    expected_length = 4
    expected_content = [100, 101, 102, 105]

    # Ejecución
    length = remove_duplicates(logs)

    # Verificación de tiempos (Fines didacticos):

    tiempo_two_pointers = timeit.timeit(lambda: remove_duplicates(logs), number=1)
    tiempo_pythonic = timeit.timeit(lambda: remove_duplicates_pythonic(logs), number=1)

    print(f"\nTiempo Two pointers (Más constante): {tiempo_two_pointers:.2e}")
    print(f"Tiempo Pythonic (Varible por hash tables): {tiempo_pythonic:.2e}")

    # Verificaciones
    assert length == expected_length  # noqa: S101
    # Verificamos solo los primeros 'length' elementos (Se ignora la basura)
    assert logs[:length] == expected_content  # noqa: S101


def test_remove_duplicates_empty() -> None:
    """Caso límite o edge case Lista vacía."""
    logs: list = []
    assert remove_duplicates(logs) == 0  # noqa: S101


CONSTANT_LENGTH = 3  # Constante para este caso


def test_remove_duplicates_no_duplicates() -> None:
    """Caso: Lista sin duplicados (no debe cambiar)."""
    logs = [1, 2, 3]
    assert remove_duplicates(logs) == CONSTANT_LENGTH  # noqa: S101
    assert logs == [1, 2, 3]  # noqa: S101
