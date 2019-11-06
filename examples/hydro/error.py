
from scipy import stats

from spux.distributions.utils import Concentrate
from spux.distributions.utils import Transform
from spux.distributions.tensor import Tensor

from spux.processes.precipitation import Precipitation
from precipitation import precipitation_coefficients
h = Precipitation (*precipitation_coefficients)

# transformation function accounting for heteroscedasticity in output measurement errors
import numpy
numpy.seterr (over = 'ignore')
beta = 25 # [L/s]
alpha = 50 # [L/s]
g = lambda y : beta * numpy.log (numpy.sinh ((alpha + y) / beta))
g0 = g (0)
dg = lambda y : 1.0 / numpy.tanh ((alpha + y) / beta)
y = lambda g : beta * numpy.arcsinh (numpy.exp (g / beta)) - alpha

# define an error model
class Error (object):

    # return an error model (distribution) for the specified prediction and parameters
    def distribution (self, prediction, parameters):

        # specify error distributions using stats.scipy for each observed variable independently
        # available options (univariate): https://docs.scipy.org/doc/scipy/reference/stats.html
        distributions = {}

        # here, collapse the left tail of the normal distribution at xi = h.inverse (0) and then apply the tranformation T
        distribution_xi = stats.norm (loc = prediction [r'$\xi$'], scale = parameters [r'$\sigma_\xi$'])
        distribution_xi_c = Concentrate (distribution_xi, left = h.inverse (0))
        distributions ['x'] = Transform (distribution_xi_c, T = h.evaluate, Ti = h.inverse, dTi = h.d_inverse)

        # truncated normal distribution limits need to be specified in the unscaled (standard) form
        a = (g0 - g (prediction ['y'])) / parameters [r'$\sigma_y$']
        # distributions ['g'] = stats.truncnorm (a = a, b = float ('inf'), loc = prediction ['g'], scale = parameters [r'$\sigma_y$'])
        distribution_g = stats.truncnorm (a = a, b = float ('inf'), loc = g (prediction ['y']), scale = parameters [r'$\sigma_y$'])
        # transform the distribution to the y-space
        distributions ['y'] = Transform (distribution_g, T = y, Ti = g, dTi = dg)

        # construct a joint distribution for a vector of independent parameters by tensorization
        distribution = Tensor (distributions)

        return distribution

    # # custom transformation function for the observation (prediction or dataset)
    # def transform (self, observation, parameters):

    #     observation = copy (observation)
    #     if r'$\xi$' not in observation:
    #         observation [r'$\xi$'] = h.inverse (observation ['x'])
    #     del observation ['x']
    #     observation ['g'] = g (observation ['y'])
    #     del observation ['y']
    #     return observation

error = Error ()
