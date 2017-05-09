from player import Player
from player import generate_player

import matplotlib.pyplot as plt

def player_group(n):
	for i in range(0, n):
		p = generate_player()
		print(str(p) + '|| Overall: ' + str(p.overall_rating()) + '\n')

def pos_comparison():
	p = generate_player()
	print(p)
	print('Player plays: ' + str(p.pos()) + ' and has overall: ' + str(p.overall_rating()))
	for pos in Pos.pos_list():
		print('If player played ' + str(pos) + ' then overall would be ' + str(p.overall_rating_new_pos(pos)))

def plot_overall_ratings(n):
	ratings = []
	lowest = 100; highest = 0
	for i in range(0, n):
		r = generate_player().overall_rating()
		if r > highest: highest = r 
		if r < lowest: lowest = r
		ratings.append(r)

	n, bins, patches = plt.hist(ratings, highest - lowest, facecolor='green')

	plt.xlabel('Overall Rating')
	plt.ylabel('Numbers')
	plt.axis([0, 100, 0, 60])

	plt.show()

plot_overall_ratings(1000)