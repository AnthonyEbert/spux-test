
module load cray-mpich
module load cray-python/3.6.5.1
module list

export PYTHONPATH=$PYTHONPATH:~/repos/spux
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_RUN_PATH

unset _JAVA_OPTIONS

/usr/bin/time -p -o timer.dat srun -n 41 python -m mpi4py script_parallel.py legacy

