
# load posterior samples
from spux.io import loader
samples, infos = loader.reconstruct ()

# burnin
burnin = 150

# plotting class
from spux.plot.mpl import MatPlotLib
plot = MatPlotLib (samples, infos, burnin = burnin)

# plot unsuccessful posteriors
plot.unsuccessfuls ()

# plot resets of stuck chains
plot.resets ()

# compute and report approximated maximum a posterior (MAP) parameters estimate
plot.MAP ()

# plot samples
plot.parameters ()

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

# plot timestamps
plot.timestamps ()
timestamps = [ "evaluate", "routings", "wait"]
timestamps += [ "init", "init sync", "run", "run sync"]
timestamps += ["errors", "errors sync", "resample", "resample sync"]
plot.timestamps (keys = timestamps, suffix = '-cherrypicked')

# === remove burnin

samples, infos = loader.tail (samples, infos, batch = burnin)
plot = MatPlotLib (samples, infos, burnin = burnin, tail = burnin)
plot.MAP ()

# plot autocorrelations
plot.autocorrelations ()

# plot marginal posterior distributions
plot.posteriors ()

# plot pairwise joint posterior distributions
plot.posteriors2d ()

# plot pairwise joint posterior distribution for selected parameter pairs
plot.posterior2d (r'$\sigma_\xi$', r'$\sigma_y$')
plot.posterior2d (r'$\tau$', 'K')

# plot posterior model predictions including observations
labels = ['x', 'y', r'$\xi$', 'S', r'$\Delta V$']
plot.predictions (labels=labels)

# plot quantile-quantile comparison of the error and residual distributions
plot.QQ ()

# compute Nash-Sutcliffe efficiency for the model
plot.NSE ('y')

# show metrics
plot.metrics ()

# report status
plot.status ()

# generate report
from spux.report import generate
authors = r'Jonas {\v S}ukys'
generate.report (authors)