#!/usr/bin/env python3

from integer import Integer
from time import perf_counter as pc

times = []

for i in range(30, 46):
    f = Integer(i)
    start = pc()
    f.fib()
    end = pc()
    times.append(round(end-start, 4))

results = open("fib_times.txt", "w")
for time in times:
    results.write("%s\n" % time)
results.close()