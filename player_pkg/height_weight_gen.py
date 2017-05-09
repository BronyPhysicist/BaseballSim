from math import cos
from math import sin
from math import degrees
from math import radians

from random import choice
from random import gauss

from statistics import mean

import matplotlib.pyplot as plt

infielder_w = [205, 260, 10]
infielder_h = [73, 80, 3]

outfielder_w = [206, 250, 10]
outfielder_h = [73, 78, 5]

catcher_w = [215, 255, 10]
catcher_h = [72.5, 77, 6]

pitcher_w = [213, 290, 10]
pitcher_h = [74.5, 82, 5]

def hw_list(w_params, h_params):
	w_mean = w_params[0]; w_max = w_params[1]; w_sigma = w_params[2]; w_min = w_max - 2*(w_max - w_mean)
	h_mean = h_params[0]; h_max = h_params[1]; h_sigma = h_params[2]; h_min = h_max - 2*(h_max - h_mean)

	w_list = []; h_list = []; w_plot = []; h_plot = []; data_size = 10000

	lowest = 0; leftest = 0; highest = 0; rightest = 0
	for n in range(0, data_size):
		w_0 = gauss(0, w_sigma); h_0 = gauss(0, h_sigma)

		theta = radians(45)

		w_1 = w_0*cos(theta) - h_0*sin(theta)
		h_1 = w_0*sin(theta) + h_0*cos(theta)

		if w_1 < leftest: leftest = w_1
		if w_1 > rightest: rightest = w_1
		if h_1 < lowest: lowest = h_1
		if h_1 > highest: highest = h_1

		w_list.append(w_1); h_list.append(h_1)

	w_scale = (w_max - w_min)/(rightest - leftest)
	h_scale = (h_max - h_min)/(highest - lowest)

	point_list = []
	for n in range(0, data_size):
		w_f = w_scale*(w_list[n] - leftest) + w_min; h_f = h_scale*(h_list[n] - lowest) + h_min 
		w_plot.append(w_f)
		h_plot.append(h_f)
		point_list.append( (int(w_f), int(h_f)) )

	return point_list

infield_hw  = hw_list(infielder_w, infielder_h)
outfield_hw = hw_list(outfielder_w, outfielder_h)
catcher_hw  = hw_list(catcher_w, catcher_h)
pitcher_hw  = hw_list(pitcher_w, pitcher_h)

def catcher_height_weight():  return choice(catcher_hw)
def infield_height_weight():  return choice(infield_hw)
def outfield_height_weight(): return choice(outfield_hw)
def pitcher_height_weight():  return choice(pitcher_hw)
