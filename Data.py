from math import *
import Data 

# Irreversible Reaction 
teta = 10
cf = 1 
Tf = 300 
Tc = 290 
J = 100 
alpha = 1.95e-4 
k10 = 300 
N = 25.2
yf = Tf/J/cf
yc = Tc/J/cf
F_coolant = 370 



# Steady state conditions (SP) 
y1sp = 0.4
y2sp = 3.29
us = 370 

a1 = 1
a2 = 1
a3 = 1e-3

u0 = F_coolant 
I0 = (a1*(1-y1sp)**2+a2*(yf-y2sp)**2+a3*(u0-us)**2)

t_span = 20 #min 
n_steps = 20
t_step = t_span/n_steps
n_integral = 10
n_runs = 10 

