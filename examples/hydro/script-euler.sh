
echo `date +%Y-%m-%d_%H:%M:%S`

module load python
module load open_mpi/3.0.0
module list

export PYTHONPATH=$PYTHONPATH:~/repos/spux
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_RUN_PATH

alias repro="reprozip trace --continue --dont-identify-packages"

/usr/bin/time -p -o timer.dat mpirun -n 1121 --mca mpi_warn_on_fork 0 --mca pmix_server_max_wait 7200 --mca pmix_base_exchange_timeout 7200 python3 -m mpi4py script_parallel.py
#repro /usr/bin/time -p -o timer.dat mpirun -n 1121 --mca mpi_warn_on_fork 0 --mca pmix_server_max_wait 7200 --mca pmix_base_exchange_timeout 7200 python3 -m mpi4py script_split.py

#reprozip pack hydro-`date +%Y-%m-%d_%H:%M:%S`
