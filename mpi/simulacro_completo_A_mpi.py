"""
Simulacro completo A — MPI: media con reparto igual

Media de un vector de N=1200 enteros distribuido con reparto igual.
Cada proceso suma su trozo y se reduce con MPI.SUM en root.

Ejecutar: mpiexec -n 4 python simulacro_completo_A_mpi.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 1200

if rank == 0:
    data = np.arange(N, dtype='i')
else:
    data = None

local_n = N // size
local = np.empty(local_n, dtype='i')

comm.Scatter(data, local, root=0)

suma_local = np.array([local.sum()], dtype='i')

if rank == 0:
    total = np.zeros(1, dtype='i')
else:
    total = None

comm.Reduce(suma_local, total, op=MPI.SUM, root=0)

if rank == 0:
    print("Media:", total[0] / N)
