"""
MPI — Gatherv (recopilacion con trozos de distinto tamano)

Cada proceso genera rank+1 elementos. El proceso 0 recopila todos los datos
con Gatherv (trozos desiguales -> no sirve Gather).

Ejecutar: mpiexec -n 4 python ej_gatherv.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Cada proceso genera su trozo local: rank+1 elementos
local = np.array([rank * 10 + i for i in range(rank + 1)], dtype='i')

recvcounts = np.array([i + 1 for i in range(size)], dtype='i')
displacements = np.concatenate(([0], np.cumsum(recvcounts[:-1]))).astype('i')

if rank == 0:
    resultado = np.zeros(sum(recvcounts), dtype='i')
else:
    resultado = None

comm.Gatherv(local, [resultado, recvcounts, displacements, MPI.INT], root=0)

if rank == 0:
    print("Resultado:", resultado)
