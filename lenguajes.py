"""
Actividad CADI: Operaciones con Lenguajes Finitos
Funciones y lenguajes base.
"""

from functools import reduce
from typing import Iterable, Set

# Alfabeto base (según enunciado)
Sigma: Set[str] = {"a", "b", "c"}

# Lenguajes base (según enunciado)
L1: Set[str] = {"a", "b", "ab", "ba"}
L2: Set[str] = {"b", "c", "bc", "cb"}
L3: Set[str] = {"a", "b", "c"}
L4: Set[str] = {"ab", "ac"}
L5: Set[str] = {"b", "bc", "ca", "c"}

# Epsilon
EPSILON = ""


def union_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:

    conjunto: Set[str] = set()
    for L in lenguajes:
        conjunto |= set(L)
    return conjunto


def interseccion_lenguajes(*lenguajes: Iterable[str]) -> Set[str]:

    sets = [set(L) for L in lenguajes]
    if not sets:
        return set()
    return reduce(lambda A, B: A & B, sets)


def concatenacion_lenguajes(A: Iterable[str], B: Iterable[str]) -> Set[str]:

    A_set, B_set = set(A), set(B)
    return {a + b for a in A_set for b in B_set}


def concatenacion_variadica(*lenguajes: Iterable[str]) -> Set[str]:
    sets = [set(L) for L in lenguajes]
    if not sets:
        return set()
    res = sets[0]
    for nxt in sets[1:]:
        res = {x + y for x in res for y in nxt}
    return res
