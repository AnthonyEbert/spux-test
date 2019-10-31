# import SPUX components from config.py
from config import likelihood, sampler, model

# attach the specified number of parallel workers
likelihood.attach (workers = 2)
sampler.attach (workers = 2)
model.attach (workers = None)