# generate config
import script
del script

# plotting class
from spux.plot.mpl import MatPlotLib
plot = MatPlotLib ()

# plot datasets
plot.datasets ()

# plot marginal prior distributions
plot.priors ()

# plot error model distribution treating each dataset point as prediction
# and a random realization of parameters from prior distribution
from datasets import datasets
from error import h
for name, dataset in datasets.items ():
    xs = dataset ['x'] .copy (deep = 1)
    for index in dataset.index:
        xs.loc [index] = h.inverse (xs.loc [index])
    dataset [r'$\xi$'] = xs
plot.errors (predictions = datasets)

# plot distributions for the initial model values
from initial import initial
plot.distributions (initial, color='dimgray', suffix='-initial')

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')