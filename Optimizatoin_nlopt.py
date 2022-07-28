import nlopt
from numpy import *
from Equations import Objective
from Model_ import n_steps
from Result_min_time import opening_sequence


LB = zeros(n_steps)
UB = ones(n_steps)*10

opt = nlopt.opt(nlopt.LN_NEWUOA_BOUND, n_steps)

opt.set_lower_bounds(LB)
opt.set_upper_bounds(UB)
opt.set_min_objective(Objective)
opt.set_xtol_rel(1e-1)

x0 = opening_sequence*10
x = opt.optimize(x0)
minf = opt.last_optimum_value()

print("Optimum for: ", x/10)
print("minimum value: ",minf)
