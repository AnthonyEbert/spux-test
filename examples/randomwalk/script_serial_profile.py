# === SCRIPT

from script import sampler

# === SAMPLING

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux-sandbox')

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# init executor
sampler.executor.init ()

# setup sampler
sampler.setup (sandbox = sandbox, verbosity=1, index=0, seed=seed, lock=50)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (12, profile=True)

# exit executor
sampler.executor.exit ()
