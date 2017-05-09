from random import randint

fname = './female-first.txt'
surname_spaces = 15
f = open(fname)
new_data = []
for line in f.readlines():
	data = line.split()
	new_data.append( (data[0], data[1], float(data[2]) + 10**(-5)*randint(10,99)) )

f.close()

sorted_data = sorted(new_data, key=lambda tup: tup[2])

f2 = open('./female_first_adjusted.txt', 'w+')
n = 1
data_length = 8
for name in sorted_data:
	spaces = surname_spaces - len(name[0])
	extra_zeroes = data_length - len(str(name[2]))
	rank_spaces = 2 + 5 - len(str(n))
	f2.write(name[0] + ' '*spaces + str(name[1]) + ' ' + str(name[2]) + '0'*extra_zeroes + ' '*rank_spaces + str(n) + '\n')
	n += 1