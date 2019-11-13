# === BARRIER

from spux import framework
framework.barrier ()

# === INIT FRAMEWORK

from config import *

# attach the specified number of parallel workers
distance.attach (workers = 1)
sampler.attach (workers = 5)

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux', statefiles = ['positions-*.dat'])

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# setup SPUX framework
framework.setup (sandbox = sandbox, seed = seed, verbosity = 2, stdoutfile = 'stdout.txt')

# init SPUX framework
framework.init ()

# === SAMPLING

# configure sampler
sampler.configure ()
#sampler.configure (thin = 4)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (batches = 3)

# === EXIT FRAMEWORK

framework.exit ()
