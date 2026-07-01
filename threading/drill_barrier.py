"""
Threading — Barrier: punto de encuentro con hilo extra

N=10 trabajadores hacen su tarea. Un hilo monitor imprime el resumen final
solo cuando los 10 trabajadores han terminado. Barrier(N+1) porque el monitor
tambien participa en la espera.
"""

import threading
import time
import random

N = 10

barrier = threading.Barrier(N + 1)


def trabajador(i):
    time.sleep(random.uniform(0.1, 0.5))
    print(f"Trabajador {i} termina")
    barrier.wait()


def monitor():
    barrier.wait()
    print("Resumen: todos los trabajadores han terminado")


if __name__ == '__main__':
    threading.Thread(target=monitor).start()
    for i in range(N):
        threading.Thread(target=trabajador, args=(i,)).start()
