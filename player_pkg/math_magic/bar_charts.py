from random import gauss
from random import random

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def redist(val, x_lo, x_hi):
	r = random
	if val > x_hi: 
		if r < 1.0/7: return x_hi
		if r > 1.0/7 and r < 3.0/7: return x_hi - 1
		return x_hi - 2
	if val < x_lo: 
		if r < 1.0/7: return x_lo
		if r > 1.0/7 and r < 3.0/7: return x_lo + 1
		return x_lo + 2
	return val

def linear_rand_num_asc():
	r = random()
	if random() < r:
		return r
	return random()

def linear_rand_num_desc():
	r = random()
	if random() > r:
		return r 
	return random()

def plot_gaussians():
	#DATA GENERATION
	mu, sigma = 5, 1
	x_lo, x_hi = 0, 6
	x = []
	for n in range(0, 1000):
		x.append(redist(int(gauss(mu, sigma)), x_lo, x_hi))

	# the histogram of the data
	n, bins, patches = plt.hist(x, max(x) - min(x) + 1, facecolor='green', alpha=0.75)

	plt.xlabel('Index')
	plt.ylabel('Count')
	plt.axis([x_lo, x_hi + 1, 0, 750])
	plt.grid(True)

	#print(x)

	plt.show()

def plot_lin_nums():
	x = []
	for n in range(0, 10000):
		r = random()
		if r < 2.0/3:
			x.append(4 * linear_rand_num_asc())
		else:
			x.append(2*linear_rand_num_desc() + 4)

	n, bins, patches = plt.hist(x, 50, facecolor='green', alpha=0.75)

	plt.xlabel('Num')
	plt.ylabel('Count')
	plt.axis([0, 6, 0, 400])
	plt.grid(True)

	plt.show()

def lin_index():
	r = random()
	if r < 2.0/3: return 4 * linear_rand_num_asc()
	else: 2 * linear_rand_num_desc() + 4
			

	

plot_lin_nums()