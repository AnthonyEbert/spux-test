from scipy import stats
from spux.distributions.tensor import Tensor

from units import units

# return an error model (distribution) for the specified prediction and parameters
def error (prediction, parameters):

    # specify error distributions using stats.scipy for each observed variable independently
    # available options (univariate): https://docs.scipy.org/doc/scipy/reference/stats.html
    distributions = {}
    distributions ['position'] = stats.norm (prediction['position'], parameters['error'])

    # construct a joint distribution for a vector of independent parameters by tensorization
    distribution = Tensor (distributions)
    distribution.setup (units = units ['observations'])

    return distribution