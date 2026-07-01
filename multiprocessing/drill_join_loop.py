"""
Multiprocessing — Paralelismo real con Process y Value compartido

Suma 20000 enteros repartiendo en 4 procesos con Value compartido.
Demuestra que start() y join() deben ir en bucles separados para
conseguir paralelismo real (join en el mismo bucle serializa).
"""

from multiprocessing import Process, Value

datos = list(range(20_000))


def trabajo(v, sub):
    parcial = sum(sub)
    with v.get_lock():
        v.value += parcial


if __name__ == '__main__':
    v = Value('i', 0)
    n = 4
    tam = len(datos) // n
    procs = []
    for i in range(n):
        p = Process(target=trabajo, args=(v, datos[i*tam:(i+1)*tam]))
        p.start()
        procs.append(p)
    for p in procs:
        p.join()

    print("Suma:", v.value)
