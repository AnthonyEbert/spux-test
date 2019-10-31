from spux.io import loader

# exact parameters
parameters = loader.load_dict ('parameters.dat')

# exact predictions
predictions = loader.load_csv ('datasets/predictions.dat')

# exact auxiliary predictions (if auxiliary observations exist)
auxiliary = loader.load_auxiliary ('datasets/predictions-auxiliary-*.dat')

# dictionary for exact parameters and predictions
exact = {'parameters' : parameters, 'predictions' : predictions, 'auxiliary' : auxiliary}