from random import gauss
from random import random

from math_magic.distribution import rand_skill_seed
from math_magic.distribution import distro_set
from math_magic.distribution import redistribute
from math_magic.distribution import MIN_VALUE

from math_magic.linear_number import lin_index

import birthday_gen as bd

from position import Pos

'''
==========================
||Physical 			13	||
||	-Muscle		6		||
||	-Agility	4		||
||	-Reflexes	3		||
||======================||
||Mental			8	||
||	-Sharpness	4		||
||	-Strategy	1		||
||	-Calmness	3		||
||======================||
||Training			6	||
||	-Hitting	2		||
||	-Fielding	2		||
||	-Pitching	2		||
==========================
'''
#HW ratio ranges from 82/136 - 66/290

"""Helper method to use in-class"""
#def parameters():
#	index = lin_index()
#	return distro_set[index]

def parameters():
	#weights = [0.03, 0.06, 0.08, 0.12, 0.31, 0.4]
	#weights = normalize([4, 3, 3, 4, 8, 12])
	weights = normalize([7, 4, 9, 16, 25, 36])
	r = random()
	for i in range(0, len(weights)):
		if r < sum(weights[:(i+1)]): return distro_set[i]
	return distro_set[-1]

def normalize(x):
	y = []
	for val in x:
		y.append(val*1.0/sum(x))
	return y

####################
## PHYSICAL STATS ##
####################

def generate_muscle_stat(height, weight):
	hw_ratio = 1.0*height/weight
	body_term = 17.27587 - 31.9697 * hw_ratio

	params = parameters()
	return redistribute( int(rand_skill_seed(params[0], params[1]) + body_term) )

def generate_agility_stat(height, weight, birthdate, current_date):
	hw_ratio = 1.0*height/weight
	body_term = 53.2828965 * hw_ratio - 22.12645

	age = bd.years_old(birthdate, current_date)
	years_from_prime = age - 29
	age_term = -1.0/15 * years_from_prime * years_from_prime + 5

	params = parameters()
	return redistribute( int(rand_skill_seed(params[0], params[1]) + age_term + body_term) )

def generate_reflexes_stat(birthdate, current_date):
	age = bd.years_old(birthdate, current_date)
	off_peak = abs(age - 24)
	age_term = -off_peak * off_peak / 20.0

	params = parameters()
	return redistribute( int(rand_skill_seed(params[0], params[1]) + age_term) )


##################
## MENTAL STATS ##
##################

def generate_mental_stat():
	params = parameters()
	return redistribute( int(rand_skill_seed(params[0], params[1])) )


##################
##TRAINING STATS##
##################

"""This one will return 3 values for each of the training stats there are"""
def generate_training_stats(years_in_majors, position):
	exp_term = 0
	if years_in_majors == 0: pass
	else: exp_term = 16.0/(1 + 60.0/(years_in_majors * years_in_majors))

	params1 = parameters(); params2 = parameters()
	stat1 = redistribute( int(rand_skill_seed(params1[0], params1[1])) )
	stat2 = redistribute( int(rand_skill_seed(params2[0], params2[1])) )

	total = stat1 + stat2
	hitting, fielding, pitching = 0, 0, 0
	if Pos.is_infield(position):
		hitting  = int( round(total * 1.0/2.0) )
		fielding = int( round(total * 1.0/2.0) )
		pitching = MIN_VALUE
	elif Pos.is_outfield(position):
		hitting  = int( round(total * 3.0/5.0) )
		fielding = int( round(total * 2.0/5.0) )
		pitching = MIN_VALUE
	elif Pos.is_pitcher(position):
		index = int( total * 0.02999 )
		params = distro_set[index]
		pitching = redistribute( int(rand_skill_seed(params[0], params[1])) )
		fielding = redistribute( int(rand_skill_seed(distro_set[3][0], distro_set[3][1])) )
		hitting  = redistribute( int(rand_skill_seed(distro_set[1][0], distro_set[1][1])) )
	else:
		hitting  = int( round(total * 4.0/5.0) )
		fielding = int( round(total * 1.0/5.0) )
		pitching = MIN_VALUE

	return redistribute(hitting), redistribute(fielding), redistribute(pitching)


