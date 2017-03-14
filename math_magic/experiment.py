import matplotlib.pyplot as plt

from math import acos
from math import cos
from math import exp
from math import log
from math import tanh

from pitch_reader import get_pitch_speed
from pitch_reader import get_pitch_break_factor
from pitch_reader import get_pitch_name

from random import gauss

import strike_zone_locs as sz

#Batter Form:
#[Power, bat_speed, bat_acc, pit_rec, bunt]
#Pitcher Form:
#[Arm Strength, Arm Speed, Pitch Accuracy, Spin, Focus, Stamina]

def pit_accuracy_factor(pitcher, pitch_count, start_stam, pitch_spin):
	base_stam = (3.0/5.0)*cos(acos(4.0/8.0)/100.0*pitcher[p_stam])#*(1.0/2.0)*exp(log(2)*pitcher[p_ast]/100.0)
	exp_prefactor = 60*exp(-log(20)/100.0*pitcher[p_stam])
	pc_stam_arg = -pitch_count/100.0 + pitcher[p_stam]/75.0
	stam_factor = start_stam/100.0*((1 - base_stam)/2.0*tanh(exp_prefactor*pc_stam_arg) + (1 + base_stam)/2.0)
	spin_factor = 2*(1 - pitcher[p_spin]/100.0)*pitch_spin**3 + 3*(pitcher[p_spin]/100.0 - 1)*pitch_spin**2 + 1
	comp_factor = 1
	print('Stam Factor: ' + str(stam_factor) + ' at pitch ' + str(pitch_count))
	return stam_factor*spin_factor*comp_factor*(1.0/1400.0)*(10*pitcher[p_pa] + 4*pitcher[p_focus])


def plot_pitch_locs(pitcher):
	batter_height = 180
	sz_height = 0.4*batter_height
	sz_width = 43.18

	sz_w_incr = sz_width/3.0; sz_h_incr = sz_height/3.0

	sz_bounds = sz.sz_limits(sz_h_incr, sz_w_incr)
	plt.plot( ( sz_bounds[0][0], sz_bounds[1][0] ), ( sz_bounds[0][1], sz_bounds[1][1] ), 'k-')
	plt.plot( ( sz_bounds[1][0], sz_bounds[2][0] ), ( sz_bounds[1][1], sz_bounds[2][1] ), 'k-')
	plt.plot( ( sz_bounds[2][0], sz_bounds[3][0] ), ( sz_bounds[2][1], sz_bounds[3][1] ), 'k-')
	plt.plot( ( sz_bounds[3][0], sz_bounds[0][0] ), ( sz_bounds[3][1], sz_bounds[0][1] ), 'k-')

	pitch_x = []; pitch_y = []; zone_centers = sz.get_pitch_zones(sz_h_incr, sz_w_incr); zone = 'cr'

	pitch_count = 0; start_stam = 100; pitch_spin = 0

	for n in range(0, 100):
		p_x = pit_accuracy_factor(pitcher, pitch_count, start_stam, pitch_spin)
		sigma_up = sz_height*(1 - p_x)/2.0; sigma_lr = sz_width*(1 - p_x)/2.0
		pitch_x.append(gauss(zone_centers[zone][0], sigma_lr))
		pitch_y.append(gauss(zone_centers[zone][1], sigma_up))
		pitch_count += 1

	print('x: ' + str(zone_centers[zone][0]) + ' +/- ' + str(sigma_lr))
	print('y: ' + str(zone_centers[zone][1]) + ' +/- ' + str(sigma_up))

	plt.scatter(pitch_x, pitch_y)
	plt.ylim([80,-10])
	plt.xlim([80,-10])
	plt.show()

def pitch_speeds(pitcher):
	speeds = []; pitch_n = 6
	for n_pitch in range(0, 100):
		composure = 1
		arm_avg = (pitcher[p_ast] + 4*pitcher[p_asp])/500.0
		stam_factor = 0.15*exp(-log(3.0)*n_pitch/pitcher[p_stam]) + 0.85
		#print('Stam Factor: ' + str(stam_factor) + ' at pitch ' + str(n_pitch))
		speed = composure*arm_avg*get_pitch_speed(pitch_n)
		print('Pitch Speed is: ' + str(speed) + ' mph with pitch ' + get_pitch_name(pitch_n))
		speeds.append(speed)

	n, bins, patches = plt.hist(speeds, 25, facecolor='green')
	plt.show()

p_ast = 0; p_asp = 1; p_pa = 2; p_spin = 3; p_focus = 4; p_stam = 5
pitcher = [72, 95, 92, 68, 80, 50]

#plot_pitch_locs(pitcher)
pitch_speeds(pitcher)