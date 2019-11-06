import os
import numpy
import pandas

replicates = ['1', '2', '3']

datasets = {}

for replicate in replicates:

    def dataset ():
        x = numpy.genfromtxt (os.path.join ('datasets/', 'x0_%s.dat' % replicate))
        x /= 60 # change from [mm/min] to [L / (m^2 * s)]
        tx = numpy.genfromtxt (os.path.join ('datasets/', 'tx0_%s.dat' % replicate))
        inputset = pandas.DataFrame (x, columns=['x'], index=pandas.Index (tx, name='time'))
        y = numpy.genfromtxt (os.path.join ('datasets/', 'y0_%s.dat' % replicate))
        ty = numpy.genfromtxt (os.path.join ('datasets/', 'ty0_%s.dat' % replicate))
        outputset = pandas.DataFrame (y, columns=['y'], index=pandas.Index (ty, name='time'))
        return pandas.concat ([inputset, outputset], axis=1, sort=True)

    datasets [replicate] = dataset