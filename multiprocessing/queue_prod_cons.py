"""
Multiprocessing — Productor-Consumidor con Queue

Esquema productor-consumidor entre procesos: 1 productor genera 12 tareas y
3 procesos consumidores las procesan en paralelo. Senal de fin (centinela
None) por cada consumidor para que terminen de forma limpia.
"""

import time
from multiprocessing import Process, Queue

N_CONSUMIDORES = 3


def productor(q):
    for i in range(12):
        q.put(f"tarea_{i}")
    for _ in range(N_CONSUMIDORES):
        q.put(None)


def consumidor(q, id):
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumidor {id} procesa {item}")
        time.sleep(0.1)


if __name__ == '__main__':
    q = Queue()

    p = Process(target=productor, args=(q,))

    consumidores = []
    for id in range(N_CONSUMIDORES):
        c = Process(target=consumidor, args=(q, id))
        consumidores.append(c)

    p.start()
    for c in consumidores:
        c.start()

    p.join()
    for c in consumidores:
        c.join()
