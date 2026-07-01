"""
Threading — Lectores-Escritores con 3 licencias de lectura

Servidor con 3 licencias de lectura (lectores simultaneos) y 1 de escritura
(exclusiva). Semaforo de 3 para lectores + Lock para escritor (consume las 3
licencias de golpe).
"""

import threading
import time

s = threading.Semaphore(3)
l = threading.Lock()


def lector(id):
    print(f"Lector {id} esperando...")

    s.acquire()

    print(f"Lector {id} leyendo datos...")
    time.sleep(1)
    s.release()


def escritor(id):
    print(f"Escritor {id} esperando acceso exclusivo...")
    with l:
        s.acquire()
        s.acquire()
        s.acquire()
        print(f"Escritor {id} MODIFICANDO datos...")
        time.sleep(2)
        s.release()
        s.release()
        s.release()


if __name__ == "__main__":
    lectores = [threading.Thread(target=lector, args=(i,)) for i in range(5)]
    escritores = [threading.Thread(target=escritor, args=(i,)) for i in range(2)]

    for h in lectores + escritores:
        h.start()

    for h in lectores + escritores:
        h.join()

    print("Todos los lectores y escritores han terminado.")
