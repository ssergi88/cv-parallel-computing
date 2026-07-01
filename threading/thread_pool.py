"""
Threading — ThreadPoolExecutor para procesamiento de archivos

Procesa una lista de archivos en paralelo con hilos usando
concurrent.futures.ThreadPoolExecutor. Map bloquea hasta tener
todos los resultados y preserva el orden de entrada.
"""

import time
from concurrent.futures import ThreadPoolExecutor


def procesar_archivo(nombre):
    time.sleep(0.2)
    return f"OK_{nombre}"


if __name__ == '__main__':
    archivos = [f"file_{i}.dat" for i in range(20)]

    with ThreadPoolExecutor(max_workers=4) as pool:
        res = list(pool.map(procesar_archivo, archivos))

    print(res)
