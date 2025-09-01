"""
Ejercicios de Unión de Lenguajes
Imprime los resultados de los 10 ejercicios de la sección de UNIÓN.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lenguajes import union_lenguajes, L1, L2, L3, L4, L5

def fmt(S):
    return "{" + ", ".join(sorted(S)) + "}"

def main():
    ejercicios = {}

    # 1)
    ejercicios[1] = union_lenguajes(L1, L2)

    # 2) 
    ejercicios[2] = union_lenguajes(L1, L3)

    # 3) 
    ejercicios[3] = union_lenguajes(L2, L3)

    # 4
    ejercicios[4] = union_lenguajes(L4, L5)

    # 5) 
    ejercicios[5] = union_lenguajes(L1, L2, L3)

    # 6)
    A6 = {"cad","aca","ad"}
    B6 = {"a","d","c"}
    ejercicios[6] = union_lenguajes(A6, B6)

    # 7) 
    A7 = {"10","01","11"}
    B7 = {"0","1"}
    C7 = {"00","10"}
    ejercicios[7] = union_lenguajes(A7, B7, C7)

    # 8) 
    ejercicios[8] = union_lenguajes(L1, L2)
    pertenece_abc = "abc" in ejercicios[8]

    # 9) 
    ejercicios[9] = union_lenguajes(L4, L5)
    pertenece_a = "a" in ejercicios[9]

    # 10) 
    ejercicios[10] = union_lenguajes({"x","y"}, {"y","z"})

    # Impresión de resultados
    for k in range(1, 11):
        print(f"Ejercicio {k}: {fmt(ejercicios[k])}")
        if k == 8:
            print(f'   ¿"abc" pertenece? -> {pertenece_abc}')
        if k == 9:
            print(f'   ¿"a" pertenece? -> {pertenece_a}')

if __name__ == "__main__":
    main()
