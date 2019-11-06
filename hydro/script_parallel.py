
# === BARRIER

from spux import framework
framework.barrier ()

# === INIT FRAMEWORK

from config import *

# attach the specified number of parallel workers
model.attach (workers = None)
likelihood.attach (workers = 2)
replicates.attach (workers = 2)
sampler.attach (workers = 2)

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux-sandbox')

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# setup SPUX framework
outputdir = '/cluster/scratch/sukysj/spux-hydro'
stdoutfile = 'stdout.txt'
framework.setup (sandbox = sandbox, seed = seed, verbosity = 2, outputdir = outputdir, stdoutfile = stdoutfile)

# init SPUX framework
framework.init ()

# === SAMPLING

# configure sampler
sampler.configure (lock = 50)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (24)

# === EXIT FRAMEWORK

framework.exit ()