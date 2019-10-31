from scipy import stats
from spux.distributions.tensor import Tensor
distributions = {'position' : stats.norm (loc = 10, scale = 2)}
units = {'position' : 'm'}

inputset = {}
inputset ['time'] = 0
inputset ['initial'] = Tensor (distributions, units = units)