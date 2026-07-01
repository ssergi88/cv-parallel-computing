# Parallel & Distributed Computing — Algorithms and Benchmarks

Ejercicios de programacion paralela y distribuida desarrollados como practicas
universitarias. Cubren los paradigmas principales: memoria compartida (threading),
multiprocesamiento y paso de mensajes (MPI).

## Content

### `threading/`
Problemas clasicos de concurrencia con hilos: barbero dormilon, lectores-escritores
con 3 licencias de lectura, pool de hilos para procesamiento de archivos y barrera
de sincronizacion.

### `multiprocessing/`
Paralelismo real con `multiprocessing`: Pool.map para paralelizar operaciones
independientes y productor-consumidor con Queue entre procesos. Incluye ejemplo
de Value compartido con exclusion mutua.

### `mpi/`
Ejercicios de MPI con mpi4py: Scatterv/Gatherv, Reduce/Allreduce, conversion de
comunicacion punto-a-punto a colectiva, y tres simulacros completos que combinan
reparto desigual, reduccion y recogida de resultados.

## Stack
- Python 3
- threading, multiprocessing (stdlib)
- mpi4py, numpy

## How to run

```bash
pip install -r requirements.txt
```

Scripts de threading y multiprocessing:
```bash
python threading/barber.py
python multiprocessing/pool_map.py
```

Scripts de MPI (requieren MPI instalado en el sistema):
```bash
mpiexec -n 4 python mpi/ej_scatterv_gatherv.py
mpiexec -n 4 python mpi/simulacro_completo_A_mpi.py
```

## Key concepts
- Speedup y balanceo de carga
- Comunicacion colectiva (Scatterv, Gatherv, Reduce, Allreduce)
- Sincronizacion con primitivas: Lock, Event, Semaphore, Barrier
- Reparto desigual: sendcounts y displacements

## Disclaimer

Estos ejercicios fueron desarrollados como practicas universitarias en el Grado
de Ciencia de Datos (UV).
