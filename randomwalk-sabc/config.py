# MODEL
from spux.models.randomwalk import Randomwalk
model = Randomwalk (dt = 0.1)

# DISTANCE
from spux.distances.euclidean import Euclidean
distance = Euclidean (alpha = 2)

# SAMPLER
from spux.samplers.sabc import SABC
sampler = SABC (ensemble_size = 100, batch_size = 10, epsilon_init = 200)

# ASSEMBLE ALL COMPONENTS
from dataset import dataset
from inputset import inputset
from spux.distances.statistics.identity import identity as statistic
from timeset import timeset
from prior import prior
from spux import framework
from units import units
distance.assign (model, statistic, dataset, inputset, timeset)
sampler.assign (distance, prior)
framework.assign (sampler, units)