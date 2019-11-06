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
# use Replicates aggregator to combine likelihood with multiple data sets
from spux.aggregators.replicates import Replicates
replicates = Replicates ()

# SAMPLER
# construct EMCEE sampler
from spux.samplers.emcee import EMCEE
sampler = EMCEE (chains=4)
#sampler = EMCEE (chains=32)

# ASSIGN COMPONENTS
from datasets_synthetic import datasets
from inputsets_synthetic import inputsets
from prior import prior
from error import error
from units import units
from spux import framework
likelihood.assign (model, error)
replicates.assign (likelihood, datasets, inputsets)
sampler.assign (replicates, prior)
framework.assign (sampler, units)