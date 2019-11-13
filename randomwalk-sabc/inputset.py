from scipy import stats
from spux.distributions.tensor import Tensor
distributions = {'position' : stats.norm (loc = 10, scale = 2)}

inputset = {}
inputset ['time'] = 0
inputset ['initial'] = Tensor (distributions)

from units import units
inputset ['initial'] .setup (units = units ['observations'])
