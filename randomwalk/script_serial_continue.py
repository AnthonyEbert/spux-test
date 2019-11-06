# === SCRIPT

from script import sampler

# === INITIALIZATION

# load the most recent info
from spux.io import loader
info = loader.last ("infos-*.dat")

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

# setup sampler (shift the starting index and load the last obtained feedback)
setup = {}
setup ['index'] = info ['index'] + 1
setup ['feedback'] = info ['feedback']
sampler.setup (sandbox = sandbox, verbosity = 1, seed = seed, lock = 50, thin = 10, **setup)

# init sampler (load the last used parameters and their scaled posteriors)
sampler.init (initial = info ['parameters'], posteriors = info ['posteriors'])

# generate samples from posterior distribution
sampler (4)

# exit executor
sampler.executor.exit ()
