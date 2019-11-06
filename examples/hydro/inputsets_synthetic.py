
# construct input sets

from datasets_synthetic import datasets

inputsets = {}
for replicate in datasets.keys ():
    inputsets [replicate] = datasets [replicate] .index [0]