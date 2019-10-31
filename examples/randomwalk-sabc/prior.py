# specify prior distributions using stats.scipy for each parameter (independently)
# available options (univariate): https://docs.scipy.org/doc/scipy/reference/stats.html

from scipy import stats

from spux.distributions.tensor import Tensor
from spux.utils import transforms

from units import units

distributions = {}

# model parameters
distributions ['drift'] = stats.uniform (loc=-1, scale=2)
distributions ['volatility'] = stats.uniform (loc=0.2, scale=1)

# construct a joint distribution for a vector of independent parameters by tensorization
prior = Tensor (distributions)
prior.setup (units = units ['parameters'])
