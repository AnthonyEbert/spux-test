
# import profile analysis methods
from spux.plot import profile

# export profile stats
profile.report ('output/profile.pstats')

# plot profile callgraph
profile.callgraph ('output/profile.pstats')
