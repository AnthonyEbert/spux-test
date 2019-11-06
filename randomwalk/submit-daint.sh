#!/bin/bash -l
#
#SBATCH --account=d97
#SBATCH --job-name="spxrndwlkpy"
#SBATCH --time=00:05:00
#SBATCH --ntasks=145
#SBATCH --ntasks-per-core=1
#SBATCH --cpus-per-task=1
#SBATCH --partition=debug
#SBATCH --constraint=mc
#SBATCH --distribution=block
#
module load cray-python/3.6.5.1
export PYTHONPATH=/users/${USER}/sfw/spux_dev_marco:${PYTHONPATH}
TMPDIR=/scratch/snx3000/${USER}/spux_dev_marco/randomwalk/a1
OUTDIR=/scratch/snx3000/${USER}/spux_dev_marco/randomwalk/a1
#
if [ ! -d $TMPDIR ] ; then
  mkdir $TMPDIR
fi
if [ ! -d $OUTDIR ] ; then
  mkdir $OUTDIR
fi
#
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
#
srun --ntasks=${SLURM_NTASKS} --hint=nomultithread --cpu-bind=rank python3 -m mpi4py script_parallel.py --connector legacy >& ${OUTDIR}/tmplog
#
