from player import generate_player
from player import Player

def generate_league(n_players):
	league = []
	for i in range(0, n_players):
		league.append(generate_player())
	league = sorted(league, key=lambda x: x.overall_rating(), reverse=True)
	return league

league = generate_league(1200)

f = open('league.txt', 'w+')

for player in league:
	f.write(str(player) + '\n')

f.close()