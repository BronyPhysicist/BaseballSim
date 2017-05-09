from random import random
from random import gauss
from random import choice

from math import pow
from math import exp
from math import factorial
from math import sqrt

import matplotlib.pyplot as plt

MAX_VALUE = 100
MIN_VALUE = 12

distro_set = [(20, 36), (36, 66), (50, 83), (72,94), (85, 103), (95, 110)]

def distro(val, n, x_max):
	a = n*1.0/(x_max - n)
	norm_coeff = a/factorial(n)
	poly_factor = -a * val + n*(a + 1)
	exp_factor = exp(-poly_factor)
	#print('Sharpness = ' + str(a) + '; Normalization = ' + str(norm_coeff) + '; Polynomial = ' + str(poly_factor) + '; Exp Factor = ' + str(exp_factor) )
	if poly_factor == 0 or exp_factor == 0: return 0.0
	return norm_coeff * pow(poly_factor, n) * exp_factor

def prob_values(n, x_max):
	probs = []
	for x in range(1, x_max + 1):
		x_lo = x - 0.5; x_hi = x + 0.5
		f_lo = distro(x_lo, n, x_max)
		f_hi = distro(x_hi, n, x_max)
		square_area   = f_lo*(x_hi - x_lo)
		triangle_area = 0.5*abs(f_hi - f_lo)*(x_hi - x_lo)
		probs.append(square_area + triangle_area)
	return probs

def random_color():
	terms = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
	return '#' + choice(terms) + choice(terms) + choice(terms) + choice(terms) + choice(terms) + choice(terms)

def plot_different_distros(distro_set):
	plotted = []; labels = []
	for dist in distro_set:
		n = dist[0]; x_max = dist[1]; dist_data = []; levels = []; cdf = []
		for i in range(1, x_max):
			levels.append(i)
			dist_data.append(distro(i, n, x_max))
			if len(cdf) == 0: cdf.append(distro(i, n, x_max))
			else: cdf.append(cdf[-1] + distro(i, n, x_max))

		color = random_color()
		r_line = plt.scatter(levels, dist_data, c=color)
		plt.plot(levels, dist_data, c=color)
		plotted.append(r_line); labels.append('n = '+str(n) + '; x_max=' + str(x_max))
	
	#crit = plt.plot(gens, criticality_line(seed_n, len(gens) - 1), c='r', linewidth='3'); plotted.append(crit); labels.append('crit')
	plt.xlabel('Skill Level', fontsize=20); plt.ylabel('Prob Mass', fontsize=20)
	plt.tick_params(axis='both', which='major', labelsize=20); plt.tick_params(axis='both', which='minor', labelsize=8)
	plt.title('Probability Mass', fontsize=24)
	#plt.yscale('log')
	ax = plt.gca(); ax.set_xlim([0, 100])
	plt.legend(plotted, labels, loc="upper left")
	plt.show()

def rand_skill_seed(n, x_max):
	r = random()
	prob_estimates = prob_values(n, x_max); cum_prob = 0
	for i in range(0, len(prob_estimates)):
		cum_prob += prob_estimates[i]
		if r < cum_prob: return redistribute(i + 1)
	return redistribute(x_max)

def redistribute(value):
	if value > MAX_VALUE: return MAX_VALUE
	elif value < MIN_VALUE: return MIN_VALUE
	else: return value


#mean = 90; x_max = 90
#print(n_and_a(mean, x_max))
#n = 84; x_max = 90
#print(prob_values(n, x_max))
#for i in range(1, x_max + 1):
#	print('Distro at x=' + str(i) + ': ' + str(distro(i, n, x_max)))


plot_different_distros(distro_set)

#for i in range(0, 100):
#	print(rand_skill_seed(n, x_max))