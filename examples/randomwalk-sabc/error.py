from scipy import stats
from spux.distributions.tensor import Tensor

from units import units

from auxiliary import auxiliary
from spux.distributions.merge import Merge

# define an error model
class Error (object):

    def __init__ (self, scalar = True):

        self.scalar = scalar

    # auxiliary dataset loader (optional)
    def auxiliary (self, time):

        return auxiliary (time)

    # return an error model (distribution) for the specified prediction and parameters
    def distribution (self, prediction, parameters):

        # specify error distributions using stats.scipy for each observed variable independently
        # available options (univariate): https://docs.scipy.org/doc/scipy/reference/stats.html
        distributions = {}
        if self.scalar:
            distributions ['position'] = stats.norm (prediction['position'], parameters['error'])
        else:
            distributions ['position'] = stats.norm (prediction['values']['position'], parameters['error'])

        # construct a joint distribution for a vector of independent parameters by tensorization
        distribution = Tensor (distributions)
        distribution.setup (units = units ['observations'])

        if self.scalar:
            return distribution
        else:
            distribution_auxiliary = None # construct your auxiliary distribution here
            return Merge (distribution, distribution_auxiliary)

error = Error ()
