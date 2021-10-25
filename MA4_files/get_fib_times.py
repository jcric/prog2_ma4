#!/usr/bin/env python3

from integer import Integer
import sys 
from time import perf_counter as pc

n = int(sys.argv[1])
results = open("fib_times.txt", "w")
times = []

for i in range(30, n):
    f = Integer(n)
    start = pc()
    f.fib()
    end = pc()
    f.__del__()
    times.append(round(end-start, 4))

for time in times:
    results.write("%s\n" % time)
results.close()