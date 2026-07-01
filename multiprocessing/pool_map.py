"""
Multiprocessing — Pool.map

Calcula el cuadrado de una lista de numeros en paralelo usando Pool.map.
Se elige map porque bloquea hasta tener resultados completos, preserva el
orden de entrada y es la opcion mas simple para un solo argumento por tarea.
"""

import time
from multiprocessing import Pool, cpu_count


def calcular(x):
    time.sleep(0.1)      # Simula computo intensivo
    return x * x


if __name__ == '__main__':
    datos = list(range(20))

    n = min(cpu_count() * 2, len(datos))
    with Pool(n) as p:
        resultados = p.map(calcular, datos)

    print(resultados)
