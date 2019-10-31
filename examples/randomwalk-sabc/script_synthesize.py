from spux.models.randomwalk import Randomwalk
from spux.utils.seed import Seed
from spux.utils.sandbox import Sandbox
from error import error
from inputset import inputset
from timeset import timeset
from spux.io.loader import load_dict
import numpy

parameters = load_dict ('parameters.dat')

exact ['error'] = 0.5

dt = 0.1
steps = 250
snapshots = 1 + 50
start = inputset ['time']
end = start + steps * dt
snapshots = numpy.linspace (start, end, snapshots)

model = Randomwalk (dt = dt)
sandbox = Sandbox ('sandbox-synthesize')
seed = Seed (4)

from spux.utils import synthesize
synthesize.generate (model, parameters, snapshots, error = error, inputset = inputset, timeset = timeset, sandbox = sandbox, seed = seed)