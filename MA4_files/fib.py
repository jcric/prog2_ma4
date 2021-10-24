from time import perf_counter as pc
import matplotlib.pyplot as plt 


def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))
    
ns = []
times = []

for n in range(30, 45):
    start = pc()
    fib_py(n)
    end = pc()
    ns.append(n)
    times.append(round(end-start, 4))


plt.plot(ns, times, 'r')
plt.title('Time for recursive fibonacci in Python')
plt.xlabel('n')
plt.ylabel('Seconds')
plt.savefig('fib_py_30to45.png')
#plt.show()
