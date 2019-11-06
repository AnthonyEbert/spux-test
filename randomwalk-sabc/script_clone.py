from spux.models.randomwalk import Randomwalk
from exact import exact
from inputset import inputset

model = Randomwalk ()
parameters = exact ['parameters']
time_clone = 20
time_compare = 40
sandbox = None

from spux.utils import testing
testing.clone (model, parameters, time_clone, time_compare, inputset = inputset, sandbox = sandbox)