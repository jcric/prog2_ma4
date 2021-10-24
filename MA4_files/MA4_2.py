#!/usr/bin/env python3

from integer import Integer
import sys 

n = int(sys.argv[1])

def main():
	f = Integer(n)
	print(f.get())
	print(f.fib())

if __name__ == '__main__':
	main()