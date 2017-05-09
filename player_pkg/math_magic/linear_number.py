from random import gauss
from random import random

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

def lin_index():
	r = random()
	if r < 2.0/3: return int(4 * linear_rand_num_asc())
	else: return int(2 * linear_rand_num_desc() + 4)