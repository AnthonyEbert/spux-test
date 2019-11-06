
# paths to result directories
paths = {}
paths [1] = 'randomwalk-200p-10s-1c/output'
paths [8] = 'randomwalk-2000p-10s-8c/output'
paths [50] = 'randomwalk-2000p-100s-50c/output'
paths [200] = 'randomwalk-2000p-100s-200c/output'
paths [1000] = 'randomwalk-2000p-100s-1000c/output'

# runtime scaling factors
factors = {}
factors [1] = 10
factors [8] = 1
factors [50] = 1
factors [200] = 1
factors [1000] = 1

# select batch and chain
batch = 0
chain = 0

# load posterior samples
from spux.io import loader
timingsdict = {}
for workers, path in paths.items ():
    timings = loader.reconstruct (samplesfiles = None, infosfiles = None, directory = path)
    timingsdict [workers] = timings [batch] ['infos'] [chain]

# plotting class
from spux.plot.mpl import MatPlotLib
plot = MatPlotLib ()

# plot scaling
plot.scaling (timingsdict, factors)
