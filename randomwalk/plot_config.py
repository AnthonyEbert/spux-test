# generate config
from spux.utils import shell
shell.importer ('config.py')

# plotting class
from spux.plot.mpl import MatPlotLib
from exact import exact
plot = MatPlotLib (exact = exact)

# plot dataset
plot.dataset ()

# plot marginal prior distributions
plot.priors ()

# plot marginal error model distributions
plot.errors ()

# plot marginal prior distributions for the initial model values
from inputset import inputset
exact_initial = exact ['predictions'] .iloc [0]
plot.distributions (inputset ['initial'], samples = {'exact' : exact_initial}, suffix = '-initial')

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')