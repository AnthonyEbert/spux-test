
# === BARRIER

from spux import framework
framework.barrier ()

# === MODEL

from hydro import Hydro
from precipitation import precipitation_coefficients
from initial import initial

model = Hydro (precipitation_coefficients, initial, dt=10, integrator='RKSSP', numbify=0)
framework.assign (model)

# === INIT FRAMEWORK

model.attach (workers = None)

from spux.utils.seed import Seed
from spux.utils.sandbox import Sandbox

sandbox = Sandbox ('sandbox-synthesize')
seed = Seed (1)

# setup SPUX framework
framework.setup (sandbox = sandbox, seed = seed, verbosity = 1, outputdir = 'datasets_synthetic')

# init SPUX framework
framework.init ()

# === SYNTHESIS

from exact import exact
# from error import error
error = None

parameters = exact ['parameters']
steps = 10000
period = 100
snapshots = range (0, period + steps, period)
replicates = 3
inputsets = [lambda : 0] * replicates

from spux.utils import synthesize
synthesize.generate (model, parameters, snapshots, error = error, inputsets = inputsets)

# === EXIT FRAMEWORK

framework.exit ()