# specify prior distributions using stats.scipy for each parameter independently
# available options (univariate): https://docs.scipy.org/doc/scipy/reference/stats.html
from scipy import stats

from spux.distributions.tensor import Tensor
from spux.utils import transforms

from error import dg

distributions = {}

distributions ['A'] = stats.lognorm (**transforms.logmeanstd (logm = 11815.8, logs = 1181.6)) # [m^2]
distributions ['K'] = stats.lognorm (**transforms.logmeanstd (logm = 284.4, logs = 57.6)) # [s] - derived from lognorm (0.079, 0.016) [hr]
distributions [r'$x_{gw}$'] = stats.lognorm (**transforms.logmeanstd (logm = 2.05, logs = 0.013)) # [L/s]
distributions [r'$-\zeta_1$'] = stats.lognorm (**transforms.logmeanstd (logm = 0.25, logs = 0.094)) # [L/s]
distributions [r'$-\zeta_2$'] = stats.lognorm (**transforms.logmeanstd (logm = 0.84, logs = 0.019)) # [L/s]
distributions [r'$-\chi_1$'] = stats.lognorm (**transforms.logmeanstd (logm = 0.68, logs = 0.019)) # [L/s]
distributions [r'$\chi_2$'] = stats.lognorm (**transforms.logmeanstd (logm = 0.077, logs = 0.01)) # [L/s]
distributions [r'$\sigma_y$'] = stats.lognorm (**transforms.logmeanstd (logm = 4.1 * dg (50), logs = 0.41 * dg (50))) # [L/s]
distributions [r'$\tau$'] = stats.lognorm (**transforms.logmeanstd (logm = 1000, logs = 200)) # [s]

# original distribution LN (0.4, 0.2) is for sigma^2_xi (note the square)
# to get the distribution for sigma_xi, we first compute the mean and scale of the associated normal distribution, and then divide by 2
normal = transforms.logmeanstd (logm = 0.4, logs = 0.2)
normal ['scale'] = normal ['scale'] ** 0.5
normal ['s'] = normal ['s'] / 2
distributions [r'$\sigma_\xi$'] = stats.lognorm (**normal) # [L/(s*m^2)]

# construct a joint distribution for a vector of independent parameters by tensorization
prior = Tensor (distributions)
