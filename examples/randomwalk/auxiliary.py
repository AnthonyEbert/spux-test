
from spux.io import loader

# method to load auxiliary dataset for the specified time
def auxiliary (time):
    return loader.load ('datasets/dataset-auxiliary-*.dat' % str(time), verbosity = 0)