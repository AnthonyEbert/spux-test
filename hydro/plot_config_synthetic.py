# generate config
from spux.utils import shell
shell.importer ('config_synthetic.py')

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
from initial import initial
exact_initial = exact ['predictions'] .iloc [0]
plot.distributions (initial, samples = {'exact' : exact_initial}, suffix='-initial')

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')