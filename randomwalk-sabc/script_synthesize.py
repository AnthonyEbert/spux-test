
# === BARRIER

from spux import framework
framework.barrier ()

# === MODEL

from spux.models.randomwalk import Randomwalk
dt = 0.1
model = Randomwalk (dt = dt)
framework.assign (model)

# === INIT FRAMEWORK

model.attach (workers = None)

from spux.utils.seed import Seed
from spux.utils.sandbox import Sandbox

sandbox = Sandbox ('sandbox-synthesize')
seed = Seed (4)

# setup SPUX framework
framework.setup (sandbox = sandbox, seed = seed, verbosity = 1, outputdir = 'datasets')

# init SPUX framework
framework.init ()

# === SYNTHESIS

from error import error
from inputset import inputset
from timeset import timeset
from spux.io.loader import load_dict
import numpy

parameters = load_dict ('exact_parameters.dat')

steps = 250
snapshots = 1 + 50
start = inputset ['time']
end = start + steps * dt
snapshots = numpy.linspace (start, end, snapshots)

from spux.utils import synthesize
synthesize.generate (model, parameters, snapshots, error = error, inputset = inputset, timeset = timeset)

# === EXIT FRAMEWORK

framework.exit ()