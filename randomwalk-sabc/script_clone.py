
# === BARRIER

from spux import framework
framework.barrier ()

# === MODEL

from spux.models.randomwalk import Randomwalk
model = Randomwalk ()
framework.assign (model)

# === INIT FRAMEWORK

model.attach (workers = None)

from spux.utils.sandbox import Sandbox
sandbox = Sandbox ('sandbox-clone')

# setup SPUX framework
framework.setup (sandbox = sandbox, verbosity = 1)

# init SPUX framework
framework.init ()

# === CLONING

from exact import exact
from inputset import inputset

parameters = exact ['parameters']
time_clone = 20
time_compare = 40

from spux.utils import testing
testing.clone (model, parameters, time_clone, time_compare, inputset = inputset)

# === EXIT FRAMEWORK

framework.exit ()