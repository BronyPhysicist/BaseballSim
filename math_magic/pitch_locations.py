from pitch_reader import get_pitch_spin

def pit_accuracy_factor(stam_skill, spin_skill, acc_skill, focus_skill, pitch_count, start_stam, pitch_spin):
	base_stam = (3.0/5.0)*cos(acos(4.0/8.0)/100.0*stam_skill)#*(1.0/2.0)*exp(log(2)*pitcher[p_ast]/100.0)
	exp_prefactor = 60*exp(-log(20)/100.0*stam_skill)
	pc_stam_arg = -pitch_count/100.0 + stam_skill/75.0
	stam_factor = start_stam/100.0*((1 - base_stam)/2.0*tanh(exp_prefactor*pc_stam_arg) + (1 + base_stam)/2.0)
	spin_factor = 2*(1 - spin_skill/100.0)*pitch_spin**3 + 3*(spin_skill/100.0 - 1)*pitch_spin**2 + 1
	comp_factor = 1
	print('Stam Factor: ' + str(stam_factor) + ' at pitch ' + str(pitch_count))
	return stam_factor*spin_factor*comp_factor*(1.0/1400.0)*(10*acc_skill + 4*focus_skill)

def get_pitch_loc():
	batter_height = 180
	sz_height = 0.4*batter_height
	sz_width = 43.18

	sz_w_incr = sz_width/3.0; sz_h_incr = sz_height/3.0

	zone_centers = sz.get_pitch_zones(sz_h_incr, sz_w_incr); zone = 'cr'
	
	p_x = pit_accuracy_factor(pitcher, pitch_count, start_stam, pitch_spin)
	sigma_up = sz_height*(1 - p_x)/2.0; sigma_lr = sz_width*(1 - p_x)/2.0
	pitch_x.append(gauss(zone_centers[zone][0], sigma_lr))
	pitch_y.append(gauss(zone_centers[zone][1], sigma_up))
