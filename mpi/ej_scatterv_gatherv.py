"""
MPI — Scatterv -> operar -> Gatherv (round-trip)

El proceso 0 tiene un vector de N=17 enteros. Reparto desigual: los primeros
N%size reciben un elemento de mas. Cada proceso suma 100 a sus elementos.
Se recogen los resultados en orden.

Ejecutar: mpiexec -n 4 python ej_scatterv_gatherv.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 17

if rank == 0:
    B = np.arange(1, N + 1, dtype='i')
else:
    B = None

base = N // size
resto = N % size

sendcounts = np.array([base + (1 if i < resto else 0) for i in range(size)], dtype='i')
displacements = np.concatenate(([0], np.cumsum(sendcounts[:-1]))).astype('i')

local = np.empty(sendcounts[rank], dtype='i')
comm.Scatterv([B, sendcounts, displacements, MPI.INT], local, root=0)

local += 100

if rank == 0:
    resultado = np.empty(N, dtype='i')
else:
    resultado = None

comm.Gatherv(local, [resultado, sendcounts, displacements, MPI.INT], root=0)

if rank == 0:
    print("Resultado:", resultado)
