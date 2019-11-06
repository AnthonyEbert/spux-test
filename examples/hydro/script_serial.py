# === SCRIPT

from script import sampler

# === SAMPLING

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# init executor
sampler.executor.init ()

# setup sampler
sampler.setup (verbosity=1, index=0, seed=seed)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (12)

# exit executor
sampler.executor.exit ()