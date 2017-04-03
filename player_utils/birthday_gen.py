from random import random
from random import randint

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'calendar'))
from date import Day
from date import Month
from date import Date

from calendar_module import start_date

#start_date = Date(Day.WED, Month.APR, 1, 2006)

age_numbers = [6, 17, 40, 79, 114, 138, 158, 167, 156, 150, 123, 101, 92, 70, 41, 29, 24, 17, 7, 4, 4, 1]
age_probs = []
tot_players = sum(age_numbers)
tot_prob = 0
for freq in age_numbers:
	tot_prob += freq*1.0/tot_players
	age_probs.append(tot_prob)
youngest = 21

def generate_birthdate(cur_year):
	r = random()
	age = 0
	for i in range(0, len(age_probs)):
		if r < age_probs[i]:
			age = i + youngest
			break

	birth_year = cur_year - age
	birth_month = Month.rand_month()
	birth_day_num = randint(1, birth_month.num_days())
	birth_day = Day.rand_day()

	new_date = Date(birth_day, birth_month, birth_day_num, birth_year)
	new_date.correct_day(start_date)
	return new_date