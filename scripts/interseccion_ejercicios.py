"""
Ejercicios de Intersección de Lenguajes
Imprime los resultados de los 10 ejercicios de la sección de INTERSECCIÓN.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lenguajes import interseccion_lenguajes, L1, L2, L3, L4, L5

def fmt(S):
    return "{" + ", ".join(sorted(S)) + "}"

def main():
    ejercicios = {}

    # 1) 
    ejercicios[1] = interseccion_lenguajes(L1, L2)

    # 2) 
    ejercicios[2] = interseccion_lenguajes(L1, L3)

    # 3) 
    ejercicios[3] = interseccion_lenguajes(L2, L3)

    # 4) 
    ejercicios[4] = interseccion_lenguajes(L4, L5)

    # 5) 
    ejercicios[5] = interseccion_lenguajes(L1, L2, L3)

    # 6)
    A6 = {"cad","aca","ad"}
    B6 = {"a","d","c"}
    ejercicios[6] = interseccion_lenguajes(A6, B6)

    # 7)
    A7 = {"10","01","11"}
    B7 = {"0","1"}
    C7 = {"00","10"}
    ejercicios[7] = interseccion_lenguajes(A7, B7, C7)

    # 8) 
    ejercicios[8] = interseccion_lenguajes(L1, L2)
    pertenece_b = "b" in ejercicios[8]

    # 9) 
    ejercicios[9] = interseccion_lenguajes(L4, L5)
    pertenece_ac = "ac" in ejercicios[9]

    # 10) 
    ejercicios[10] = interseccion_lenguajes({"x","y"},{"y","z"})

    # Imprimir resultados
    for k in range(1, 11):
        print(f"Ejercicio {k}: {fmt(ejercicios[k])}")
        if k == 8:
            print(f'   ¿"b" pertenece? -> {pertenece_b}')
        if k == 9:
            print(f'   ¿"ac" pertenece? -> {pertenece_ac}')

if __name__ == "__main__":
    main()
