from math import cos
from math import sin
from math import degrees
from math import radians

from random import gauss

from statistics import mean

import matplotlib.pyplot as plt

def method_one():
	#w_mean = 205; w_sigma = 10
	h_mean = 73; h_sigma = 3
	spread = 8

	h_list = []; w_list = []

	data_size = 60

	for n in range(0, data_size):
		height = gauss(h_mean, h_sigma)
		h_list.append(height)
		w_list.append(gauss(0.0, spread) + (70.0/8.0)*height - 433.75)

	plt.scatter(w_list, h_list)
	plt.xlim([150, 375]); plt.ylim(66, 90)
	plt.yticks([66,72,78,84,90])
	plt.show()

def method_two():
	w_mean = 205; w_sigma = 10; w_max = 270; w_min = w_max - 2*(w_max - w_mean)
	h_mean = 73; h_sigma = 3; h_max = 80; h_min = h_max - 2*(h_max - h_mean)

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
	for n in range(0, data_size):
		w_plot.append( w_scale*(w_list[n] - leftest) + w_min )
		h_plot.append( h_scale*(h_list[n] - lowest) + h_min )

	print('Height avg: ' + str(mean(h_plot)) + ' in; Weight avg: ' + str(mean(w_plot)) + ' lbs')
	plt.scatter(w_plot, h_plot)
	#plt.xlim([-50, 150]); plt.ylim(-100, 100)
	plt.xlim([150, 375]); plt.ylim(66, 90)
	plt.yticks([66,72,78,84,90])
	plt.show()

method_two()