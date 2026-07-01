"""
MPI — Reduce vs Allreduce

Cada proceso calcula el cuadrado de su rank. Se calcula la suma total.
Parte A: Reduce (solo root conoce el total).
Parte B: Allreduce (todos conocen el total).

Ejecutar: mpiexec -n 4 python ej_allreduce.py
"""

from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

valor_local = np.array([rank ** 2], dtype='i')

# ── PARTE A: Reduce ──
if rank == 0:
    total_a = np.zeros(1, dtype='i')
else:
    total_a = None

comm.Reduce(valor_local, total_a, op=MPI.SUM, root=0)

if rank == 0:
    print(f"[Reduce]    Proceso {rank} tiene el total: {total_a[0]}")

# ── PARTE B: Allreduce ──
total_b = np.zeros(1, dtype='i')
comm.Allreduce(valor_local, total_b, op=MPI.SUM)

print(f"[Allreduce] Proceso {rank} tiene el total: {total_b[0]}")
