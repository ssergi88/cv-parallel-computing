"""
Threading — Barbero dormilon

Sincronizacion con 2 Events: un barbero duerme hasta que llega un cliente;
el cliente avisa y espera a que el barbero termine el corte. Gestion de
silla con Lock para acceso exclusivo.
"""

import threading
import time
import random

N_CLIENTES = 5

silla = threading.Lock()
evt_llegada = threading.Event()
evt_corte = threading.Event()


def barbero():
    while True:
        evt_llegada.wait()
        evt_llegada.clear()

        print('Barbero: cortando el pelo')
        time.sleep(random.uniform(0.5, 1.5))
        print('Barbero: corte terminado')

        evt_corte.set()


def cliente(id):
    print(f'Cliente {id}: llega a la barberia')

    with silla:
        print(f'Cliente {id}: se sienta en la silla')

        evt_llegada.set()
        evt_corte.wait()
        evt_corte.clear()

        print(f'Cliente {id}: se levanta y se va')


if __name__ == '__main__':
    threading.Thread(target=barbero, daemon=True).start()

    clientes = []
    for i in range(N_CLIENTES):
        t = threading.Thread(target=cliente, args=(i,))
        clientes.append(t)
        t.start()
        time.sleep(random.uniform(0.1, 0.4))

    for t in clientes:
        t.join()

    print('Todos los clientes atendidos')
