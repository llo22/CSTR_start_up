from numpy import *
from Model_ import *
from Data import n_runs

R = empty([n_runs,1])

# Brute forcing on n_runs
for r in range(0,n_runs):

    result_time_index = where(y2_m[:,r] >= y2sp + 0.001)[0]
    R[r,0] = t_m[result_time_index[0],r]
    
minimum_time_index = min(range(len(R)), key=R.__getitem__)
print('Minimum time required:  %f seconds' %R[minimum_time_index,0])
print('Best run: %f' %minimum_time_index)

# Best first guess from brute forcing 
opening_sequence = OP_tens[:,0,minimum_time_index]
opening_sequence = opening_sequence.detach().numpy()

print('Best first guess:', opening_sequence)