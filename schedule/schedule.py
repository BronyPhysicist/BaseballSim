'''
Created on Jun 5, 2016

@author: Brendan Hassler
'''
import random

name = 0; abb = 1; div = 2


#Schedule Params
N_DIV_GAMES = 10; N_LEAGUE_GAMES = 8; N_IL_GAMES = 2
N_GAMES = N_DIV_GAMES*4 + N_LEAGUE_GAMES*10 + N_IL_GAMES*15
N_DAYS = 190

'''

#Training Params
N_DIV_GAMES = 3; N_LEAGUE_GAMES = 2; N_IL_GAMES = 1
N_GAMES = N_DIV_GAMES*4 + N_LEAGUE_GAMES*10 + N_IL_GAMES*15
N_DAYS = 60
'''

null = 'NULL'; rest = 'REST'


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

def same_division(team, opp): return team[div] == opp[div]

def same_league(team, opp): return team[div] != opp[div] and team[div][:2] == opp[div][:2]

def opp_league(team, opp): return team[div] != opp[div] and team[div][:2] != opp[div][:2]

def n_games_to_play(team, opp):
    if same_division(team, opp): return N_DIV_GAMES
    if same_league(team, opp): return N_LEAGUE_GAMES
    if opp_league(team, opp): return N_IL_GAMES

def init_sched():
    sched = {}
    for n in range(0, N_DAYS):
        sched[n] = []
    return sched

def has_game_that_day(sched, team, day):
    for game in sched[day]:
        if game[0] == team[abb] or game[1] == team[abb]: return True
    return False

def has_rest_game_that_day(sched, team, day):
    for game in sched[day]:
        if game[0] == team[abb] and game[1] == rest: return True
    return False

def has_real_game_that_day(sched, team, day):
    for game in sched[day]:
        if (game[0] == team[abb] and game[1] != rest) or game[1] == team[abb]: return True
    return False

def doubled_up(sched, team, day):
    games = 0
    for game in sched[day]:
        if game[0] == team[abb] or game[1] == team[abb]:
            games += 1
    return games > 1

def count_games_with_team(sched, team, teams):
    gc = {}
    for opp in teams:
        if team == opp: continue
        gc[opp[abb]] = 0
    for day in range(0, N_DAYS):
        for game in sched[day]:
            if game[1] == rest: continue
            if game[0] == team[abb]:
                gc[game[1]] += 1
            elif game[1] == team[abb]:
                gc[game[0]] += 1
    return gc

def games_in_a_row(sched, team, day):
    cons_games = 0; day_clone = day - 1
    while day_clone >= 0 and has_real_game_that_day(sched, team, day_clone):
        cons_games += 1; day_clone -= 1
    return cons_games

#So far probabilities are hard-coded
def rest_game_probs(sched, team, day):
    cons_games = games_in_a_row(sched, team, day)
    #        0  1  2  3    4    5   6    7    8    9    10   11   12   13   14   15   16   17   18   19   20
    probs = [0, 0, 0, .05, .05, 10, .15, .22, .25, .30, .34, .39, .46, .54, .64, .70, .75, .80, .90, .95, 1.0]
    if cons_games > 20: return 1
    else: return probs[cons_games]

def has_games_left(sched, team, opp, teams):
    gc = count_games_with_team(sched, team, teams)
    #print('Team: ' + team[abb] + ': ' + str(gc))
    if same_division(team, opp): return N_DIV_GAMES - gc[opp[abb]]
    elif same_league(team, opp): return N_LEAGUE_GAMES - gc[opp[abb]]
    else: return N_IL_GAMES - gc[opp[abb]]
    
def pick_available_opp(sched, team, teams, day):
    opps = []
    for opp in teams:
        if opp == team: continue
        already_scheduled = not has_game_that_day(sched, opp, day)
        if already_scheduled and has_games_left(sched, team, opp, teams): opps.append(opp)
    if len(opps) == 0: return null
    return random.choice(opps)

def validate(sched, teams):
    '''
    A schedule is invalid if:
        1. A team has two games on the same day
        2. The number of games between teams is NOT equal to their counter value
        3. A team does not play N_GAMES.
    '''
    #Test 1
    for team in teams:
        for day in range(0, N_DAYS):
            if doubled_up(sched, team, day):
                print('VALIDATION FAILED')
                print('On day ' + str(day) + ' team ' + team[abb] + ' is doubled-up.')
                return False
    #Test 2
    for team in teams:
        for opp in teams:
            if opp == team: continue
            if has_games_left(sched, team, opp, teams):
                print('VALIDATION FAILED')
                print('Team ' + team[abb] + ' and ' + opp[abb] + ' still have games left to play.')
                return False
    #Test 3
    for team in teams:
        tot_games = 0
        for day in range(0, N_DAYS):
            if has_game_that_day(sched, team, day) and not has_rest_game_that_day(sched, team, day): tot_games += 1
        if tot_games < N_GAMES:
            print('VALIDATION FAILED')
            print('Team ' + team[abb] + ' isn\'t scheduled for enough games.')
            return False
        if tot_games > N_GAMES:
            print('VALIDATION FAILED')
            print('Team ' + team[abb] + ' is scheduled for too many games.')
            return False
    print('Validation was successful.')
    return True

def write_schedule(sched):
    f = open('../TextDocs/schedule.txt', 'w+')
    f.write('League Schedule\n=========================\n\n')
    for day in range(0, N_DAYS):
        f.write('Day ' + str(day) + '\n===========\n')
        for game in sched[day]:
            f.write(game[1] + ' at ' + game[0] + '\n')
        f.write('\n')
    f.close()
    
def teams_are_uneven(home_game_ct, teams):
    for team in teams:
        if home_game_ct[team[abb]] != N_GAMES/2: return True
    return False

def count_home_games(sched, teams):
    home_game_ct = {}
    for team in teams:
        home_game_ct[team[abb]] = 0
    for day in range(0, N_DAYS):
        for game in sched[day]:
            if game[1] != rest: home_game_ct[game[0]] += 1
    return home_game_ct
    
def home_game_tuning(sched, teams):
    print('Tuning schedule. May take a while.')
    hgc = count_home_games(sched, teams)
    ideal = N_GAMES/2
    iters = 0
    while teams_are_uneven(hgc, teams) and iters < 10:
        for day in range(0, N_GAMES):
            games_to_swap = []
            for game in sched[day]:
                if game[1] == rest: continue
                if hgc[game[0]] > ideal and hgc[game[1]] < ideal:
                    games_to_swap.append(game)
                    hgc = count_home_games(sched, teams)
            for game in games_to_swap:
                sched[day].remove(game)
                sched[day].append( (game[1], game[0]) )
        iters += 1
    return sched
            
#Schedule structure:
#A dictionary indexed by days, which contains a list of games happening that day.
#Games are tuples with home team at 0 and away team at 1.
def schedule():
    sched = init_sched()
    teams = get_teams_no_FA('../TextDocs/cities.csv')
    
    for day in range(0, N_DAYS):
        print('Scheduling Day ' + str(day))
        random.shuffle(teams)
        for team in teams:
            if has_game_that_day(sched, team, day): continue
            opp = pick_available_opp(sched, team, teams, day)
            rg = rest_game_probs(sched, team, day)
            if random.random() < rg or opp == null: sched[day].append( (team[abb], rest) )
            else:
                if random.random() < 0.5: sched[day].append( (team[abb], opp[abb]) )
                else: sched[day].append( (opp[abb], team[abb]) )
    
    if validate(sched, teams): print('Returning valid schedule.')
    else: print('Returning invalid schedule.')
    return sched

sched = home_game_tuning(schedule(), get_teams_no_FA('../TextDocs/cities.csv'))
#sched = schedule()
write_schedule(sched)