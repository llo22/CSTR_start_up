from Data import * 
from numpy import * 
from math import * 
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def modelODE(t,y,x_i): 
    y1 = y[0]
    y2 = y[1]

    u = x_i/10*F_coolant 
    r = k10*exp(-N/y2)*y1

    dy1dt = 1/teta*(1-y1) - r
    dy2dt = 1/teta*(yf-y2) + r -alpha*u*(y2-yc)
    dydt = [dy1dt,dy2dt]

    return dydt

def modelODE_(t,y,x_i,mode): 
    y1 = y[0]
    y2 = y[1]
    I =  y[2]
    x_i = float(''.join(map(str,x_i)))
    u = x_i/10*F_coolant 
    r = k10*exp(-N/y2)*y1

    dy1dt = 1/teta*(1-y1) - r
    dy2dt = 1/teta*(yf-y2) + r -alpha*u*(y2-yc)
    if mode ==(3,): 
        I = (a1*(y1-y1sp)**2+a2*(y2-y2sp)**2)
    if mode ==(1,): 
        I = (a2*(y2-y2sp)**2)
    if mode==(2,): 
        I = (a1*(y1-y1sp)**2)

    dydt = [dy1dt,dy2dt,I]

    return dydt



def Objective(x,grad):
    grad = empty 
    I = zeros(n_steps)
    y1 = zeros([n_steps,n_integral])
    y2 = zeros([n_steps,n_integral])
    y3 = zeros([n_steps,n_integral])

    integration_initial_values = zeros([n_steps,3])
    integration_initial_values[0,:] = [1,yf,I0]

    for i_step in range(0,n_steps):
        
        # Integration 
        x_i = x[i_step]
        #u = x_i/10*F_coolant 
        x_i = (x[i_step]),
        
    
        X0_new = integration_initial_values[i_step,:]
        t_in = t_step*i_step
        t_out = t_step*(1+i_step)
        time = linspace(t_in,t_out,n_integral)

        if y1[i_step-1,-1]<=y1sp+0.1 and y1[i_step-1,-1]>=y1sp-0.1: 
            mode = (1,)
            sol = solve_ivp(modelODE_,(t_in,t_out), X0_new ,t_eval=time,args=(x_i,mode))
        elif y2[i_step-1,-1]<=y2sp+1 and y2[i_step-1,-1]>=y2sp-1:
            mode = (2,)
            sol = solve_ivp(modelODE_, (t_in,t_out), X0_new ,t_eval=time,args=(x_i,mode))
        else: 
            mode = (3,)
            sol = solve_ivp(modelODE_, (t_in,t_out), X0_new ,t_eval=time,args=(x_i,mode))

        t = sol.t
        y1[i_step,:] = sol.y[0,:]
        y2[i_step,:] = sol.y[1,:]
        y3[i_step,:] = sol.y[2,:]
        I[i_step] = y3[i_step,-1] 


        # Update values
        if i_step < n_steps-1:
            integration_initial_values[i_step+1,:] = [y1[i_step,-1],y2[i_step,-1],y3[i_step,-1]]
        else:
            break
        
        #I = (a1*(y1-y1sp)**2+a2*(y2-y2sp)**2+a3*(u-us)**2)

    F = sum(I)
        
    
    return float(F)

