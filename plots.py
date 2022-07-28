import matplotlib.pyplot as plt
from Model_ import *
from Result_min_time import *
from new_results import *

#%% 
# Profile with brute forcing 
# fig = plt.figure(1)
fig,(ax1,ax2) = plt.subplots(2)
fig.suptitle('Brute forcing')
ax1 = fig.add_subplot(111)
ax1.set_xlabel('t (s)')
ax1.set_ylabel('Temperature profile', color='tab:blue')
ax1.plot(t_m[:,minimum_time_index],y2_m[:,minimum_time_index])

# Valve opening profile with brute forcing 
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('%',color = color)
ax2.set_ylim([0,1])
ax2.step(t_m[:,minimum_time_index],opening_sequence_array[:,minimum_time_index], color=color)
ax2.set_title('Valve Opening')
fig.tight_layout()

#%% 
# Profile for the optimized results
fig = plt.figure(2)
ax1 = fig.add_subplot(111)
ax1.set_xlabel('t (s)')
ax1.set_ylabel('Concentration profile', color='tab:blue')
ax1.plot(t_opt, Y2_opt)

# Valve opening profile with brute forcing 
ax2 = ax1.twinx()
color = 'tab:orange'
ax2.set_ylabel('%',color = color)
ax2.set_ylim([0,1])
ax2.step(t_opt,x_opt, color=color)
ax2.set_title('Valve Opening')
fig.tight_layout()


plt.figure(3)
plt.plot(t_opt,Y1_opt)

plt.show()


