"""
Threading — Pool de hilos para procesamiento de archivos

Procesa una lista de archivos en paralelo usando Pool de multiprocessing.
Se elige map porque bloquea hasta tener resultados completos, preserva el
orden de entrada y es la opcion mas simple para un solo argumento por tarea.
"""

import time
from multiprocessing import Pool, cpu_count


def procesar_archivo(nombre):
    time.sleep(0.2)      # Simula computo intensivo
    return f"OK_{nombre}"


if __name__ == '__main__':
    archivos = [f"file_{i}.dat" for i in range(20)]

    n = min(cpu_count(), len(archivos))
    with Pool(n) as p:
        res = p.map(procesar_archivo, archivos)

    print(res)
