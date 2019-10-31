# === BARRIER

from spux import framework
framework.barrier ()

# === INIT FRAMEWORK

from config import *

# attach the specified number of parallel workers
model.attach (workers = None)
likelihood.attach (workers = 8)
sampler.attach (workers = 16)

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux', statefiles = ['positions-*.dat'])

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# setup SPUX framework
outputdir = '/cluster/scratch/sukysj/spux-randomwalk'
stdoutfile = 'stdout.txt'
framework.setup (sandbox = sandbox, seed = seed, verbosity = 2, outputdir = outputdir, stdoutfile = stdoutfile)

# init SPUX framework
framework.init ()

# === SAMPLING

# configure sampler
sampler.configure (lock = 75)
#sampler.configure (lock = 75, thin = 4)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (15000)

# === EXIT FRAMEWORK

framework.exit ()