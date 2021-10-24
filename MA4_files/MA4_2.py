#!/usr/bin/env python3

from integer import Integer
import sys 
from time import perf_counter as pc

n = int(sys.argv[1])

def main():
	f = Integer(n)
	start = pc()
	print(f"Number {n} in the fibonacci is {f.fib()}.")
	end = pc()
	print(f"Calculting this took {round(end-start, 4)} seconds.")

if __name__ == '__main__':
	main()