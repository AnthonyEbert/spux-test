
# === distribution for the initial model values

# prior expert knowledge: always start with no measured rain
from spux.processes.precipitation import Precipitation
from precipitation import precipitation_coefficients
h = Precipitation (*precipitation_coefficients)
xi0_m = h.inverse (0) # [L/(s*m^2)]
xi0_s = 1 # [L/(s*m^2)]

# prior expert knowledge: always start with a discharge driven by ground water
y0_m = 2.05 # [L/s] - the mean of the x_gw from the prior.py
y0_s = 1 # [L/s] - assume an uninformative prior with large extent

# specify distributions for each needed initial variable accordingly
from spux.utils import transforms
from scipy import stats
from spux.distributions.tensor import Tensor
distributions = {}
distributions [r'$\xi$'] = stats.norm (loc = xi0_m, scale = xi0_s) # [L/(s*m^2)]
distributions ['y'] = stats.lognorm (**transforms.logmeanstd (logm = y0_m, logs = y0_s)) # [L/s]

# construct a tensor distribution for all variables
initial = Tensor (distributions)

from units import units
initial.setup (units = units ['observations'])