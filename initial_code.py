import numpy as n
n_trials=10**7
n_hits=0
points = n.random.uniform(-1.0,1.0,(10**7,2))
for a in points:
    if a[0]**2 + a[1]**2 <1 :
       n_hits+=1
approx_pi=4*n_hits/n_trials
print(approx_pi)
