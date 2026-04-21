import sys
from Model import *
from functions import argparser
Jij = {'0-0': 1,'1-1': 1,'1-0': 1,'0-1': 1}


if __name__ == '__main__':
	params = argparser()
	print(params, flush=True)
	m = Model(**params)
	for i in params:
		if hasattr(m, i):
			print(i, getattr(m, i))
		else:
			print('Model has no attribute', i)
	sys.exit(0)