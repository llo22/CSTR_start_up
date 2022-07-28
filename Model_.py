from Data import *
from Equations import * 
from numpy import *
from scipy.integrate import solve_ivp 
import torch as T
import random
import matplotlib.pyplot as plt 

# Inizialitation
Y1 = zeros([n_steps, n_integral])
Y2 = zeros([n_steps, n_integral])

Time = empty([n_steps,n_integral])
Opening_values = zeros([n_steps,n_integral])
X0 = [1,yf]
i = 0

# Generating empty tensors 
tensor = T.ones(())
Y1_tens = tensor.new_empty((n_steps,n_integral,n_runs))
Y2_tens = tensor.new_empty((n_steps,n_integral,n_runs))
OP_tens = tensor.new_empty((n_steps,n_integral,n_runs))
Time_tens = tensor.new_empty((n_steps,n_integral,n_runs))


for r in range(0,n_runs): 
    t_until_stop = 0

    for i_step in range(0,n_steps):
        
        y1_sol = zeros([1,n_integral])
        y2_sol = zeros([1,n_integral])
        t_sol = linspace(t_step*i_step,t_step*(1+i_step),n_integral)
        
        # Valve opening
        x = random.randint(0,10)
        x_i = x
        x_i = (x_i,)
        
        # Integration         
        t_in = t_step*i_step
        t_out = t_step*(1+i_step)
        time = linspace(t_in,t_out,n_integral)
        
        sol = solve_ivp(modelODE, (t_in,t_out), X0, t_eval=time,args=x_i)
        
        t = sol.t
        y1 = sol.y[0,:]
        y2 = sol.y[1,:]
            
        x_array = ones(n_integral)*x_i/10
        
        # Saving Data 
        Y1[i_step,:] = y1
        Y2[i_step,:] = y2
        Time[i_step,:] = t
        Opening_values[i_step,:] = x_array
        
        # Update values
        X0 = [y1[-1],y2[-1]]
        
        if i_step == (n_steps-1): 
            X0 = [1,yf]

    # Worst case scenario 
    if y1[-1] > 1: 
        Time += 1 


    # Storing data for each run
    Y1_t = T.from_numpy(Y1)
    Y2_t = T.from_numpy(Y2)
    Y1_tens[:,:,r] = Y1_t
    Y2_tens[:,:,r] = Y2_t
    
    OP_t = T.from_numpy(Opening_values)
    OP_tens[:,:,r] = OP_t
    
    Time_t = T.from_numpy(Time)
    Time_tens[:,:,r] = Time_t
    

# Reshaping tensors into arrays 
y1_model = T.reshape(Y1_tens,(n_steps*n_integral,n_runs))
y1_m = y1_model.detach().numpy()

y2_model = T.reshape(Y2_tens,(n_steps*n_integral,n_runs))
y2_m = y2_model.detach().numpy()

t_model = T.reshape(Time_tens,(n_steps*n_integral,n_runs))
t_m = t_model.detach().numpy()

opening_sequence_array = T.reshape(OP_tens,(n_steps*n_integral,n_runs))
opening_sequence_array = opening_sequence_array.detach().numpy()

# plt.plot(t_m[:,0],y1_m[:,0])
# plt.figure()
# plt.plot(t_m[:,0],y2_m[:,0])
# plt.show()
