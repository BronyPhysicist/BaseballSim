from schedule_v3 import full_schedule
from schedule_v3 import get_teams_no_FA
from schedule_v3 import get_team_abbrevs

name = 0; abb = 1; div = 2
rest = 'REST'

fname = '../TextDocs/cities.csv'

def get_team_sched(sched, team):
	team_sched = []
	for gameday in sched:
		for game in gameday:
			if team in game: team_sched.append(game)
	return team_sched

def n_real_games(team_sched):
	real_games = 0
	for game in team_sched:
		if rest in game: continue
		real_games += 1
	return real_games

def n_real_home_games(team_sched, team):
	home_games = 0
	for game in team_sched:
		if team == game[0] and game[1] != rest: home_games += 1
	return home_games

def n_real_away_games(team_sched, team):
	away_games = 0
	for game in team_sched:
		if game[1] == team: away_games += 1
	return away_games

def rest_games_at_end(team_sched):
	n = -1
	while team_sched[n][1] == rest: n -= 1
	return -(n + 1)

def count_rests(team_sched):
	rests = 0
	for game in team_sched:
		if game[1] == rest: rests += 1
	return rests

def analysis(fname):
	full_teams = get_teams_no_FA(fname)
	sched = full_schedule(fname)
	for team in full_teams:
		team_sched = get_team_sched(sched, team[abb])
		print('Analyzing ' + team[name] + ' Schedule...')
		print('\tHas ' + str(n_real_games(team_sched)) + ' games.')
		print('\t' + str(n_real_home_games(team_sched, team[abb])) + ' home games.')
		print('\t' + str(n_real_away_games(team_sched, team[abb])) + ' away games.')
		print('\t' + 'Team has ' + str(rest_games_at_end(team_sched)) + ' rests at the end of their season.')
		print('\t' + 'Team has ' + str(count_rests(team_sched) - rest_games_at_end(team_sched)) + ' rests in season.')
		print('\n')

analysis(fname)
