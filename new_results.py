from Data import *
from numpy import *
import math 
from scipy.integrate import solve_ivp 
from Optimizatoin_nlopt import x
import matplotlib.pyplot as plt 
from Equations import modelODE

t = linspace(0,t_span,n_steps)

# Inizialitation
Y1 = zeros([n_steps, n_integral])
Y2 = zeros([n_steps, n_integral])
Time = empty([n_steps,n_integral])
Opening_values = zeros([n_steps,n_integral])
X_opt = zeros([n_steps,n_integral])

X0 = [1,yf]
i = 0
t_until_stop = 0


for i_step in range(0,n_steps):
    
    # Valve opening
    x_opening = x[i_step]/10
    x_opening = (x_opening,)
    # Integration    
    t_in = t_step*i_step
    t_out = t_step*(1+i_step)
    time = linspace(t_in,t_out,n_integral)
    
    sol = solve_ivp(modelODE, (t_in,t_out), X0, t_eval=time, args=x_opening)
    
    t = sol.t
    y1 = sol.y[0,:]
    y2 = sol.y[1,:]

    # Saving Data 
    Y1[i_step,:] = y1
    Y2[i_step,:] = y2
    Time[i_step,:] = t

    x_array = ones(n_integral)*x_opening
    X_opt[i_step,:] = x_array
    

  # Update values
    X0 = [y1[-1],y2[-1]]

t_opt = reshape(Time,[(n_steps*n_integral),1])
Y1_opt = reshape(Y1,[(n_steps*n_integral),1])
Y2_opt = reshape(Y2,[(n_steps*n_integral),1])
x_opt = reshape(X_opt,[(n_steps*n_integral),1])


fig,(ax1,ax2) = plt.subplots(2)
fig.suptitle('Optimized profile')

ax1.plot(t_opt,Y1_opt)
ax2.plot(t_opt,Y2_opt)
ax1.plot(t_opt,multiply((ones(n_steps*n_integral)),y1sp), 'r--')
ax2.plot(t_opt,multiply((ones(n_steps*n_integral)),y2sp), 'r--')
ax1.set_xlabel('t [min]')
ax1.set_ylabel('C')
ax2.set_xlabel('t [min]')
ax2.set_ylabel('T')

plt.figure(2)
plt.plot(t_opt,x_opt)

plt.show()

