# === INIT FRAMEWORK

from config import *

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# setup SPUX framework
framework.setup (seed = seed, verbosity = 2)

# init SPUX framework
framework.init ()

# === SAMPLING

# configure sampler
sampler.configure ()

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (12)

# === EXIT FRAMEWORK

framework.exit ()