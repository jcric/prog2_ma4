#!/usr/bin/env python3

from integer import Integer
import sys 
from time import perf_counter as pc

n = int(sys.argv[1])
results = open("fib_times.txt", "w")
times = []

for i in range(30, n):
    start = pc()
    f = Integer(n)
    f.fib()
    end = pc()
    times.append(round(end-start, 4))

print(times)

for time in times:
    results.write("%s\n" % time)
results.close()