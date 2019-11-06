# exact parameters
from error import dg
parameters = {}
parameters ['A'] = 11815.8 # [m^2]
parameters ['K'] = 284.4 # [s] - derived from lognorm 0.079 [hr]
parameters [r'$x_{gw}$'] = 2.05 # [L/s]
parameters [r'$-\zeta_1$'] = 0.25 # [L/s]
parameters [r'$-\zeta_2$'] = 0.84 # [L/s]
parameters [r'$-\chi_1$'] = 0.68 # [L/s]
parameters [r'$\chi_2$'] = 0.077 # [L/s]
parameters [r'$\sigma_y$'] = 4.1 * dg (50) # [L/s]
parameters [r'$\tau$'] = 10.6 * 60 # [s]
parameters [r'$\sigma_\xi$'] = 1 # [L/(s*m^2)]

# exact predictions
import os, pandas, glob
predictions = {}
filenames = sorted (glob.glob (os.path.join ('datasets_synthetic/', 'predictions_*.dat')))
for name, filename in enumerate (filenames):
    if os.path.exists (filename):
        predictions [name] = pandas.read_csv (filename, sep=",", index_col=0)

exact = {'parameters' : parameters, 'predictions' : predictions}