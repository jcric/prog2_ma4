#!/usr/bin/env python3

from integer import Integer
import sys 
from time import perf_counter as pc
import matplotlib.pyplot as plt 

n = int(sys.argv[1])
    
ns = []
times = []

for i in range(30, n):
    start = pc()
    f = Integer(n)
    f.fib()
    end = pc()
    ns.append(n)
    times.append(round(end-start, 4))


plt.plot(ns, times, 'r')
plt.title('Time for recursive fibonacci in Python with C++')
plt.xlabel('n')
plt.ylabel('Seconds')
plt.savefig(f'fast_fib_py_30to{n}.png')
#plt.show()