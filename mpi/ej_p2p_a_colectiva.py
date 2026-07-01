"""
MPI — Convertir punto-a-punto (send/recv) en colectivas

Version original repartia datos con send/recv y recogia sumas con send/recv.
Se reescribe con dos colectivas: scatter (repartir) y reduce (juntar sumas).

Ejecutar: mpiexec -n 4 python ej_p2p_a_colectiva.py
"""

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 100

if rank == 0:
    datos = list(range(1, N + 1))
    tam = N // size
    trozos = [datos[i*tam:(i+1)*tam] for i in range(size)]
else:
    trozos = None

trozo = comm.scatter(trozos, root=0)
suma_local = sum(trozo)
total = comm.reduce(suma_local, op=MPI.SUM, root=0)

if rank == 0:
    print("Total:", total)
