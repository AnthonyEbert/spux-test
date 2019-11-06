import os
import glob
import pandas

filenames = sorted (glob.glob (os.path.join ('datasets_synthetic/', 'dataset_*.dat')))
columns = ['time','x','y']
datasets = {}
for name, filename in enumerate (filenames):
    datasets [name] = lambda : pandas.read_csv (filename, sep=",", usecols=columns, index_col=0)