import numpy as n
from decimal import Decimal, getcontext
n_trials=10**7-3
n_hits=0
getcontext().prec=100
points = n.random.uniform(Decimal(-1.0),Decimal(1.0),(n_trials,2))
for a in points:
    if a[0]**2 + a[1]**2 <1 :
       n_hits+=1
approx_pi=4*Decimal(n_hits/n_trials)
print(approx_pi)
