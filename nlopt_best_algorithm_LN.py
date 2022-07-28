from cgi import print_exception
import nlopt
from numpy import *
from Result_min_time import opening_sequence
from Model_ import n_steps
from Equations import Objective
from time import process_time

LB = zeros(n_steps)
UB = ones(n_steps)*10
x0 = opening_sequence*10
CPU_time = empty(6)
algorithms = ('NELDERMEAD', 'COBYLA', 'BOBYQA', 'NEWUOA_BOUND', 'PRAXIS', 'SBPLX')

# Non-Derivative local algorithm, pick the one with the lowest time to reach fA (i.e. taken from NelderMeal)
fA = 796.6

for i in range(0,size(algorithms)):
    t1_start = process_time()

    if i == 0: 
        opt = nlopt.opt(nlopt.LN_NELDERMEAD, n_steps)
    if i == 1: 
        opt = nlopt.opt(nlopt.LN_COBYLA, n_steps)
    if i == 2: 
        opt = nlopt.opt(nlopt.LN_BOBYQA, n_steps)
    if i == 3: 
        opt = nlopt.opt(nlopt.LN_NEWUOA_BOUND, n_steps)
    if i == 4: 
        opt = nlopt.opt(nlopt.LN_PRAXIS, n_steps)
    if i == 5: 
        opt = nlopt.opt(nlopt.LN_SBPLX, n_steps)

    opt.set_lower_bounds(LB)
    opt.set_upper_bounds(UB)
    opt.set_min_objective(Objective)
    opt.set_xtol_rel(100)
    #opt.set_param(opt,'inner_eval', 300)
    opt.set_stopval(fA)

    x = opt.optimize(x0)
    minf = opt.last_optimum_value()

    t1_end = process_time()

    print("\nOptimum for: ", x/10)
    print("minimum value: ",minf)

    CPU_time[i] = t1_end-t1_start
    
    if minf > (fA+10):
        CPU_time[i] += 100

    print("elapsed time: ", CPU_time[i])

t = min(CPU_time)
print('\nt=', t)
best_algorithm_index = min(range(len(CPU_time)), key=CPU_time.__getitem__)
print("Best algorithm: ", algorithms[best_algorithm_index])

