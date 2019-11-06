# generate config
import script_synthetic
del script_synthetic

# plotting class
from spux.plot.mpl import MatPlotLib
from exact import exact
plot = MatPlotLib (exact = exact)

# plot datasets
plot.datasets ()

# plot marginal prior distributions
plot.priors ()

# plot error model distribution treating each dataset point as prediction
# and a random realization of parameters from prior distribution
plot.errors ()

# plot distributions for the initial model values
# TODO: plot exact values too
from initial import initial
plot.distributions (initial, color='dimgray', suffix='-initial')

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')