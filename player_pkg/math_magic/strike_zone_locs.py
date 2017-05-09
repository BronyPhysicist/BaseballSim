def get_pitch_zones(h_incr, w_incr):
	return {'tl': ( (7.0/2)*w_incr, (1.0/2)*h_incr ), \
	'tm': ( (5.0/2)*w_incr, (1.0/2)*h_incr ), \
	'tr': ( (3.0/2)*w_incr, (1.0/2)*h_incr ), \
	'cl': ( (7.0/2)*w_incr, (3.0/2)*h_incr ), \
	'cm': ( (5.0/2)*w_incr, (3.0/2)*h_incr ), \
	'cr': ( (3.0/2)*w_incr, (3.0/2)*h_incr ), \
	'bl': ( (7.0/2)*w_incr, (5.0/2)*h_incr ), \
	'bm': ( (5.0/2)*w_incr, (5.0/2)*h_incr ), \
	'br': ( (3.0/2)*w_incr, (5.0/2)*h_incr )}


def sz_limits(h_incr, w_incr):
	return[( w_incr, 0 ), ( 4*w_incr, 0 ), ( 4*w_incr, 3*h_incr ), ( w_incr, 3*h_incr )]