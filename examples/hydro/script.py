# === Hydro model

# precipitation
from precipitation import precipitation_coefficients

# distribution for the initial model values
from initial import initial

# construct Hydro model
from hydro import Hydro
model = Hydro (precipitation_coefficients, initial, dt=10, integrator='RKSSP', numbify=0)

# === SPUX

# LIKELIHOOD
# construct Particle Filtering likelihood
from spux.likelihoods.pf import PF
likelihood = PF (particles=[4, 16])
#likelihood = PF (particles=16)

# REPLICATES
# use Replicates likelihood to combine likelihood with multiple data sets
from spux.likelihoods.replicates import Replicates
replicates = Replicates ()

# SAMPLER
# construct EMCEE sampler
from spux.samplers.emcee import EMCEE
sampler = EMCEE (chains=4)
#sampler = EMCEE (chains=32)

# ASSIGN COMPONENTS
from datasets import datasets
from inputsets import inputsets
from prior import prior
from error import error
likelihood.assign (model, error)
replicates.assign (likelihood, datasets, inputsets)
sampler.assign (replicates, prior)