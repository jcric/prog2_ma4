#!/usr/bin/env python3

from integer import Integer
import sys 

def main():
	f = Integer(sys.argv[1])
	print(f.get())

if __name__ == '__main__':
	main()