
echo `date +%Y-%m-%d_%H:%M:%S`

module load java
module load cray-mpich
module load cray-python/3.6.5.1
module list

export PYTHONPATH=$PYTHONPATH:~/repos/spux
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_RUN_PATH

unset _JAVA_OPTIONS

alias repro="reprozip trace --continue --dont-identify-packages"

repro /usr/bin/time -p -o timer.dat srun -n 561 python -m mpi4py script_split.py

reprozip pack hydro-`date +%Y-%m-%d_%H:%M:%S`
