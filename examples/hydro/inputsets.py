
# construct input sets

from datasets import datasets

replicates = ['1', '2', '3']

inputsets = {}
for replicate in replicates:
    inputsets [replicate] = datasets [replicate] .index [0]