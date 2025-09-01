"""
Ejercicios de Concatenación de Lenguajes
Imprime los resultados de los 10 ejercicios de la sección de CONCATENACIÓN.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lenguajes import concatenacion_lenguajes, concatenacion_variadica, L1, L2, L3, L4, L5, EPSILON

def fmt(S):
    return "{" + ", ".join(sorted(S)) + "}"

def main():
    ejercicios = {}

    # 1) 
    ejercicios[1] = concatenacion_lenguajes(L1, L2)

    # 2) 
    ejercicios[2] = concatenacion_lenguajes(L2, L3)

    # 3) 
    ejercicios[3] = concatenacion_lenguajes(L3, L1)

    # 4)
    ejercicios[4] = concatenacion_lenguajes(L4, L5)

    # 5) 
    ejercicios[5] = concatenacion_variadica(L1, L2, L3)

    # 6
    A6 = {"cad","aca","ad"}
    B6 = {"a","d","c"}
    ejercicios[6] = concatenacion_lenguajes(A6, B6)

    # 7) 
    A7 = {"10","01","11"}
    B7 = {"0","1"}
    C7 = {"00","10"}
    ejercicios[7] = concatenacion_variadica(A7, B7, C7)

    # 8)
    ejercicios[8] = concatenacion_lenguajes(L1, {EPSILON})

    # 9) 
    ejercicios[9] = concatenacion_lenguajes({EPSILON}, L2)

    # 10) 
    ejercicios[10] = concatenacion_lenguajes({"x","y"}, {"z"})

    # Imprimir resultados
    for k in range(1, 11):
        print(f"Ejercicio {k}: {fmt(ejercicios[k])}")

if __name__ == "__main__":
    main()
