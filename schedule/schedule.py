from random import shuffle

name = 0; abb = 1; div = 2

#Schedule Params
N_DIV_GAMES = 10; N_LEAGUE_GAMES = 8; N_IL_GAMES = 2; N_RESTS = 20; N_RESTS_PER_DAY = 8
N_GAMES = N_DIV_GAMES*4 + N_LEAGUE_GAMES*10 + N_IL_GAMES*15
N_DAYS = 400

rest = 'REST'

def get_teams_no_FA(fname):
    f = open(fname)
    teams = []
    for line in f.readlines():
        data = line.split(',')
        if 'Free Agents' in data[0]:
            continue
        team = [data[0] + ' ' + data[1], data[2], data[4]]
        teams.append(team)
    return teams

def get_team_abbrevs(fname):
	teams = get_teams_no_FA(fname)
	abbrevs = []
	for team in teams:
		abbrevs.append(team[abb])
	return abbrevs

def init_sched():
	sched = []
	for i in range(0, N_DAYS): sched.append([])
	return sched

def same_division(team, opp): return team[div] == opp[div]
def same_league(team, opp): return team[div] != opp[div] and team[div][:2] == opp[div][:2]
def opp_league(team, opp): return team[div] != opp[div] and team[div][:2] != opp[div][:2]

def make_games(teams):
	games = []
	for team1 in teams:
		for team2 in teams:
			if team1 == team2: continue

			if same_division(team1, team2):
				for i in range(0, N_DIV_GAMES/2): games.append( (team1[abb], team2[abb]) )
			elif same_league(team1, team2):
				for i in range(0, N_LEAGUE_GAMES/2): games.append( (team1[abb], team2[abb]) )
			else:
				for i in range(0, N_IL_GAMES/2): games.append( (team1[abb], team2[abb]) )

		for i in range(0, N_RESTS): games.append( (team1[abb], rest) )
	shuffle(games)
	return games

def has_game_that_day(sched, team, day):
	for game in sched[day]:
		if team in game: return True
	return False

def n_rest_games_that_day(sched, day):
    n_rests = 0
    for game in sched[day]:
        if rest in game: n_rests += 1
    return n_rests

def missing_teams(sched, day, fname):
	teams = get_team_abbrevs(fname)
	for game in sched[day]:
		if game[0] in teams: teams.remove(game[0])
		if game[1] in teams: teams.remove(game[1])
	return teams

def schedule(fname):
	teams = get_teams_no_FA(fname)
	sched = init_sched()
	games = make_games(teams)

	n_games = len(games)

	for n_game in range(0, n_games):
		game = games.pop()
		t1 = game[0]; t2 = game[1]
		day = 0
		if t2 != rest:
			while has_game_that_day(sched, t1, day) or has_game_that_day(sched, t2, day): day += 1
		else:
			while has_game_that_day(sched, t1, day) or n_rest_games_that_day(sched, day) >= N_RESTS_PER_DAY: day += 1
		sched[day].append(game)

	return sched

def full_schedule(fname):
	sched = schedule(fname)
	return trim_and_fill_sched(sched, fname)

def write_sched(sched, fname):
    f = open('sched.txt', 'w+')
    for day in range(0, len(sched)):
        day_str = str(day)
        if day < 10: day_str = '00' + day_str
    	elif day < 100: day_str = '0' + day_str

        sched_str = ''
        for game in sched[day]:
        	sched_str += game[0] + '@' + game[1] + ','

        sched_str = sched_str[:-1] #+ '\t\t' + str(missing_teams(sched, day, fname))
        
        f.write('Day ' + day_str + ': ' + sched_str + '\n')
    f.close()

def trim_and_fill_sched(sched, fname):
	new_sched = []
	for day in range(0,len(sched)):
		gameday = sched[day]
		if len(gameday) == 0: continue

		missing = missing_teams(sched, day, fname)
		for team in missing:
			gameday.append( (team, rest) )

		shuffle(gameday)
		new_sched.append(gameday)

	return new_sched

def fill_rests(sched, fname):
	for day in range(0, len(sched)):
		missing = missing_teams(sched, day, fname)
		for team in missing:
			sched[day].append( (team, rest) )
	return sched

def new_schedule():
	fname = '../TextDocs/cities.csv'
	sched = full_schedule(fname)
	write_sched(sched, fname)