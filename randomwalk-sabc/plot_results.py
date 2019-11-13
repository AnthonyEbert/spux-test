# === LOADING

from spux.io import loader
samples, infos = loader.reconstruct (timingsfiles = None)

# === RESULTS

# plotting class
from spux.plot.mpl import MatPlotLib
from exact import exact
plot = MatPlotLib (samples, infos, exact = exact)

# plot unsuccessful posteriors
plot.unsuccessfuls ()

# plot samples
plot.parameters ()

# plot evolution of likelihoods
plot.distances ()

# plot evolution of acceptances
plot.acceptances ()

# plot pairwise joint posterior distributions
plot.posteriors2d (suffix = '-progress')

# plot pairwise joint posterior distribution for selected parameter pairs
plot.posterior2d ('drift', 'volatility', suffix = '-progress')

# === RESULTS

samples, infos = loader.tail (samples, infos)
plot = MatPlotLib (samples, infos, exact = exact)

# compute metrics
plot.metrics ()

# plot marginal posterior distributions
plot.posteriors ()

# TODO: plot marginal posterior distributions for the initial model values (see plot_config.py for priors)

# plot pairwise joint posterior distributions
plot.posteriors2d (paths = False, initial = False)

# plot pairwise joint posterior distribution for selected parameter pairs
plot.posterior2d ('drift', 'volatility', paths = False, initial = False)

# plot posterior model predictions including datasets
plot.predictions ()

# plot quantile-quantile comparison of the error and residual distributions
plot.QQ ()

# # delete results
# del plot
# del samples
# del infos

# # === PERFORMANCE

# timings = loader.reconstruct (samplesfiles = None, infosfiles = None)
# plot = MatPlotLib (timings = timings)

# # plot runtimes
# plot.runtimes ()
# keys = ["evaluate", "init", "init sync", "run", "run sync", "errors", "errors sync", "resample", "resample sync"]
# plot.runtimes (keys, suffix = '-select')

# # plot efficiencies
# plot.efficiencies ()

# # # plot timestamps
# # plot.timestamps (batch = 'first')
# # plot.timestamps (batch = 'last')
# # timestamps = [ "evaluate", "routings", "wait"]
# # timestamps += [ "init", "init sync", "run", "run sync"]
# # timestamps += ["errors", "errors sync", "resample", "resample sync"]
# # plot.timestamps (keys = timestamps, suffix = '-select', batch = 'first')
# # plot.timestamps (keys = timestamps, suffix = '-select', batch = 'last')

# === STATUS

plot.status ()

# === REPORT

# generate report
from spux.report import generate
generate.report (authors = r'Jonas {\v S}ukys')