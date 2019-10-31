
module load python
module load open_mpi/3.0.0
module list

export PYTHONPATH=$PYTHONPATH:~/repos/spux
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$LD_RUN_PATH

/usr/bin/time -p -o timer.dat mpirun -n 145 --mca mpi_warn_on_fork 0 --mca pmix_server_max_wait 7200 --mca pmix_base_exchange_timeout 7200 python3 -m mpi4py script_parallel.py
