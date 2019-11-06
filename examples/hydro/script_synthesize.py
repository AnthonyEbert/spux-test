from hydro import Hydro
from precipitation import precipitation_coefficients
from initial import initial
from exact import exact
# from error import error
error = None

model = Hydro (precipitation_coefficients, initial, dt=10, integrator='RKSSP', numbify=0)
parameters = exact ['parameters']
steps = 10000
period = 100
times = range (0, period + steps, period)
replicates = 3
inputsets = [0] * replicates
outputdir = 'datasets_synthetic'

from spux.utils.seed import Seed
seed = Seed (1)

# from spux.utils import synthesize
from spux.utils import synthesize
synthesize.generate (model, parameters, times, error, replicates, inputsets, verbosity = 0, seed = seed, outputdir = outputdir)