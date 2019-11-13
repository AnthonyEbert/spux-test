# === FRAMEWORK

from config import *

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux', statefiles = ['positions-*.dat'])

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# setup SPUX framework
framework.setup (sandbox = sandbox, seed = seed, verbosity = 2)

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
