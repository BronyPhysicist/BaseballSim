from random import gauss

num = 0; name = 1; low_speed = 2; high_speed = 3; start_dir = 4; end_dir = 5; break_factor = 6

f = open('./pitches.csv')
pitches = []
for line in f.readlines():
	if '#' in line: continue
	tokens = line.split(',')
	pitches.append( (tokens[name], int(tokens[low_speed]), int(tokens[high_speed]), int(tokens[start_dir]), int(tokens[end_dir]), float(tokens[break_factor])) )

def get_pitch_speed(pitch_num):
	pitch = pitches[pitch_num - 1]
	mean = (pitch[low_speed] + pitch[high_speed])/2.0
	sigma = (pitch[high_speed] - mean)/2.0
	return 1.1*gauss( mean, sigma )

def get_pitch_break_factor(pitch_num):
	return pitches[pitch_num - 1][break_factor]

def get_pitch_name(pitch_num):
	return pitches[pitch_num - 1][name]

