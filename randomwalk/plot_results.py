# === load results

from spux.io import loader
samples, infos = loader.reconstruct ()

# === plot

# burnin sample batch
burnin = 75

# plotting class
from spux.plot.mpl import MatPlotLib
from exact import exact
plot = MatPlotLib (samples, infos, burnin = burnin, exact = exact)

# plot unsuccessful posteriors
plot.unsuccessfuls ()

# plot samples
plot.parameters ()

# compute Bayesian model evidence (best with burnin removed)
plot.evidence (burnin)

# plot evolution of likelihoods
plot.likelihoods ()

# plot evolution of likelihood accuracies
plot.accuracies ()

# plot evolution of likelihood particles
plot.particles ()

# plot redraw rates
plot.redraw ()

# plot evolution of acceptances
plot.acceptances ()

# plot resets of stuck chains
plot.resets ()

# === performance

# plot traffic of the PF likelihood resampling
plot.traffics ()

# plot runtimes
plot.runtimes ()
keys = ["evaluate", "init", "init sync", "run", "run sync", "errors", "errors sync", "resample", "resample sync"]
plot.runtimes (keys, suffix = '-select')

# plot efficiencies
plot.efficiencies ()

# # plot timestamps
# plot.timestamps (batch = 'first')
# plot.timestamps (batch = 'last')
# timestamps = [ "evaluate", "routings", "wait"]
# timestamps += [ "init", "init sync", "run", "run sync"]
# timestamps += ["errors", "errors sync", "resample", "resample sync"]
# plot.timestamps (keys = timestamps, suffix = '-select', batch = 'first')
# plot.timestamps (keys = timestamps, suffix = '-select', batch = 'last')

# === remove burnin

samples, infos = loader.tail (samples, infos, batch = burnin)
plot = MatPlotLib (samples, infos, burnin = burnin, tail = burnin, exact = exact)

# plot autocorrelations
plot.autocorrelations ()

# plot marginal posterior distributions
plot.posteriors ()

# TODO: plot marginal posterior distributions for the initial model values (see plot_config.py for priors)

# plot pairwise joint posterior distributions
plot.posteriors2d ()

# plot pairwise joint posterior distribution for selected parameter pairs
plot.posterior2d ('drift', 'volatility')

# plot posterior model predictions including datasets
plot.predictions ()

# compute and report effective sample size (ESS)
plot.ESS ()

# plot quantile-quantile comparison of the error and residual distributions
plot.QQ ()

# show metrics
plot.metrics ()

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')