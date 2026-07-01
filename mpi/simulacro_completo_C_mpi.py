"""
Simulacro completo C — MPI: media con reparto DESIGUAL

Media de un vector de N=30 enteros [1..30] con reparto desigual (N no
divisible entre size). Cada proceso suma su trozo local; el proceso 0
reduce las sumas parciales y calcula la media total.

Ejecutar: mpiexec -n 4 python simulacro_completo_C_mpi.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 30

if rank == 0:
    data = np.arange(1, N + 1, dtype='i')
else:
    data = None

base = N // size
resto = N % size

counts = np.array([base + (1 if i < resto else 0) for i in range(size)], dtype='i')
displ = np.concatenate(([0], np.cumsum(counts[:-1]))).astype('i')

local = np.empty(counts[rank], dtype='i')
comm.Scatterv([data, counts, displ, MPI.INT], local, root=0)

suma_local = np.array([local.sum()], dtype='i')

if rank == 0:
    total = np.zeros(1, dtype='i')
else:
    total = None

comm.Reduce(suma_local, total, op=MPI.SUM, root=0)

if rank == 0:
    print("Media:", total[0] / N)
