# === CONNECTOR INITIALIZATION

from spux.executors.mpi4py.connectors import utils
connector = utils.select ('auto')

# === SAMPLER with attached executors

from script_executors import sampler

# === SAMPLING

# SANDBOX
# use fast tmpfs
from spux.utils.sandbox import Sandbox
sandbox = Sandbox (path = '/dev/shm/spux-sandbox')

# SEED
from spux.utils.seed import Seed
seed = Seed (8)

# init executor
sampler.executor.init (connector)

# setup sampler
sampler.setup (sandbox = sandbox, verbosity = 2, index = 0, seed = seed, lock = 50, informative = True)

# init sampler (use prior for generating starting values)
sampler.init ()

# generate samples from posterior distribution
sampler (12)

# exit executor
sampler.executor.exit ()
