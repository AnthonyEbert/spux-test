# MODEL
from spux.models.randomwalk import Randomwalk
model = Randomwalk (dt = 0.1)

# LIKELIHOOD
from spux.likelihoods.pf import PF
likelihood = PF (particles = [8, 256])

# SAMPLER
from spux.samplers.emcee import EMCEE
sampler = EMCEE (chains = 64)

# ASSEMBLE ALL COMPONENTS
from error import error
from dataset import dataset
from inputset import inputset
from timeset import timeset
from prior import prior
from units import units
from spux import framework
likelihood.assign (model, error, dataset, inputset, timeset)
sampler.assign (likelihood, prior)
framework.assign (sampler, units)