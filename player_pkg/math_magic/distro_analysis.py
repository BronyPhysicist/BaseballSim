from distribution import rand_skill_seed
from distribution import distro_set
from distribution import redistribute
from distribution import distro

from random import choice
from random import random

import matplotlib.pyplot as plt

zero_lim = 0.02; one_lim = 0.1; two_lim = 0.34; three_lim = 0.64; four_lim = 0.78
weights = [0.0132, 0.0329, 0.1316, 0.1645, 0.3289, 0.3289]

def weighted_index_select():
	r = random()
	if r < zero_lim: return 0
	elif r > zero_lim  and r < one_lim  : return 1
	elif r > one_lim   and r < two_lim  : return 2
	elif r > two_lim   and r < three_lim: return 3
	elif r > three_lim and r < four_lim : return 4
	else: return 5

def plot_weighted_distro_sum():
	func = []
	for x in range(0, 101):
		sum_at_x = 0
		for i in range(0, len(distro_set)):
			n = distro_set[i][0]; x_max = distro_set[i][1]
			if x > x_max: continue
			sum_at_x += weights[i]*distro(x, n, x_max)
		func.append(sum_at_x)
	plt.plot(list(range(0, 101)), func)
	plt.show()


def distro_histo():
	valz = []
	low_value = 100
	high_value = 0
	for i in range(0, 60000):
		dist_set_n = weighted_index_select()
		n = distro_set[dist_set_n][0]; x_max = distro_set[dist_set_n][1]
		seed = rand_skill_seed(n, x_max)
		valz.append( seed )
		if seed < low_value: low_value = seed
		if seed > high_value: high_value = seed

	# the histogram of the data
	n, bins, patches = plt.hist(valz, high_value - low_value + 1)

	plt.xlabel('Skills')
	plt.ylabel('Number Made')
	plt.axis([low_value, high_value, 0, 3000])

	plt.show()

#print('Prob Masses: Zero: ' + str(zero_lim) + '; One: ' + str(one_lim - zero_lim) + '; Two: ' + str(two_lim - one_lim) + '; Three: ' + str(three_lim - two_lim) + '; Four: ' + str(four_lim - three_lim) + '; Five: ' + str(1 - four_lim))
#distro_histo()
print(sum(weights))
plot_weighted_distro_sum()