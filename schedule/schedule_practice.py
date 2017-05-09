from random import shuffle

def same_div(t1, t2): return t1[div] == t2[div]
def same_league(t1, t2): return t1[div][0] == t2[div][0] and t1[div][1] != t2[div][1]
def interleague(t1, t2): return t1[div][0] != t2[div][0]

def make_games(teams, div_games, league_games, il_games, rests):
	games = []
	for team1 in teams:
		for team2 in teams:
			if team1 == team2: continue

			if same_div(team1, team2):
				for i in range(0, div_games/2):
					games.append( team1[name] + team2[name] )
			elif same_league(team1, team2):
				for i in range(0, league_games/2):
					games.append( team1[name] + team2[name] )
			else:
				for i in range(0, il_games/2):
					games.append( team1[name] + team2[name] )

		for i in range(0, rests):
			games.append( team1[name] + rest )
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

def team_string(majors):
    s = ''
    for team in majors:
        s += team[name]
    return s

def missing_teams(sched, day, majors):
    s = team_string(majors)
    for game in sched[day]:
        if game[1] != rest: s = s.translate(None, game)
        else: s = s.translate(None, game[0])
    return s

def print_sched(sched, majors):
    for day in range(0, len(sched)):
        day_str = str(day); sched_str = str(sched[day])
        if day < 10: day_str = '0' + day_str
        if len(sched[day]) == 0: sched_str = ''
        if len(missing_teams(sched, day, majors)) == 0: print('Day ' + day_str + ': ' + sched_str)
        else: print('Day ' + day_str + ': ' + sched_str + '        ' + (7 - len(sched[day]))*'      ' + 'Missing: ' + missing_teams(sched, day, majors))

al = 'al'; nl = 'nl'
east = 'east'; west = 'west'

div1 = 'AE'; div2 = 'AW'; div3 = 'NE'; div4 = 'NW'
majors = [('A',div1), ('B',div1), ('C',div1), ('D',div2), ('E',div2), ('F',div2), ('G',div3), ('H',div3), ('I',div3), ('J',div4), ('K',div4), ('L',div4)]
rest = 'R'
name = 0; div = 1
div_games = 6; league_games = 4; il_games = 2; rests = 6

sched = []
n_days = 50
for i in range(0, n_days): sched.append([])

games = make_games(majors, div_games, league_games, il_games, rests)

n_games = len(games)

for n_game in range(0, n_games):
    game = games.pop()
    t1 = game[0]; t2 = game[1]
    day = 0
    if t2 != rest:
        while has_game_that_day(sched, t1, day) or has_game_that_day(sched, t2, day): day += 1
    else:
        while has_game_that_day(sched, t1, day) or n_rest_games_that_day(sched, day) >= 2: day += 1
    sched[day].append(game)

print_sched(sched, majors)
