# === SCRIPT with SPUX components

from script import likelihood, replicates, sampler

# === EXECUTORS

# import required executor classes
from spux.executors.mpi4py.pool import Mpi4pyPool
from spux.executors.mpi4py.ensemble import Mpi4pyEnsemble

# create executors with the specified number of parallel workers and attach them
likelihood.attach (Mpi4pyEnsemble (workers=2))
replicates.attach (Mpi4pyPool (workers=2))
sampler.attach (Mpi4pyPool (workers=2))

# display resources table
sampler.executor.table ()