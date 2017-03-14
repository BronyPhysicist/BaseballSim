from random import gauss

fname = './pitches.csv'
name = 0; low_speed = 1; high_speed = 2; start_dir = 3; end_dir = 4; break_factor = 5

f = open(fname)
pitches = {}
for line in f.readlines():
	cs_valz = line.split(',')
	if len(cs_valz) < break_factor + 2: print('Found invalid pitch. Skipping...'); continue
	pitches[int(cs_valz[0])] = ( cs_valz[name + 1], cs_valz[low_speed + 1], cs_valz[high_speed + 1], cs_valz[start_dir + 1], cs_valz[end_dir + 1], cs_valz[break_factor + 1] )

def get_pitch_speed(pitch_id):
	pitch = pitches[pitch_id]
	avg = (pitch[low_speed] + pitch[high_speed])/2.0
	stdev = (pitch[high_speed] - avg)/2.0
	return 1.1*gauss(avg, stdev)