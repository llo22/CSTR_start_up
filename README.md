# CSTR_start_up
CSTR start up with Nlopt optimization

1) 'Data', data taken from reference article to simulate start up of a CSTR by regulating the coolant flowrate for an exothermic reaction
2) 'Model_'&'Result_minimum_time', computes brute forcing on the valves opening sequence in order to have a first guess for the optimizer 
3) 'Equations' collects the CSTR ode equations and the objective function 
4) 'Optimization_nlopt', computes the optimization for the error from the set points for the system 
5) 'new_results' computes the profile with the optimized parameters 
6) 'nlopt_best_algorithm'supposevely picks the best optimizer in terms of results and CPU time for the non derivative methods included in NLopt. 

