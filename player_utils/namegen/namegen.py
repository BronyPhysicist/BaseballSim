from random import random

def make_list(name_fname):
	name_file = open(name_fname)
	name_list = []
	for line in name_file.readlines():
		data = line.split()
		name_list.append( (data[0], float(data[2])) )
	return name_list

def rand_surname():
	prob_num = random()*s_list[-1][1]
	for name_tup in s_list:
		if prob_num <= name_tup[1]: return name_tup[0]

def rand_female_name():
	prob_num = random()*f_list[-1][1]
	for name_tup in f_list:
		if prob_num <= name_tup[1]: return name_tup[0]

def rand_male_name():
	prob_num = random()*m_list[-1][1]
	for name_tup in m_list:
		if prob_num <= name_tup[1]: return name_tup[0]


s_list = make_list('./surnames_adjusted.txt')
m_list = make_list('./male_first_adjusted.txt')
f_list = make_list('./female_first_adjusted.txt')

for i in range(0, 100):
	print(rand_female_name() + ' ' + rand_surname())
	print(rand_male_name() + ' ' + rand_surname())