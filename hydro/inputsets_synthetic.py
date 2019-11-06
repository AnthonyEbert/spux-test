
# construct input sets

from datasets_synthetic import datasets

inputsets = {}
for replicate in datasets.keys ():
    inputsets [replicate] = lambda : datasets [replicate] () .index [0]