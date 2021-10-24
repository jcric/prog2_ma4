import matplotlib.pyplot as plt

with open('test.txt', 'r') as f:
    times = [int(line.strip()) for line in f]

ns = [*range(30,46,1)]


plt.plot(ns, times, 'r')
plt.title('Time for recursive fibonacci in Python using C++')
plt.xlabel('n')
plt.ylabel('Seconds')
plt.savefig('fib_py_cpp_30to45.png')
#plt.show()