'''
Created on Dec 1, 2016

@author: Brendan Hassler
'''
from enum import Enum

from random import choice
from random import randint

class Day(Enum):
    MON = ("Monday",    1)
    TUE = ("Tuesday",   2)
    WED = ("Wednesday", 3)
    THU = ("Thursday",  4)
    FRI = ("Friday",    5)
    SAT = ("Saturday",  6)
    SUN = ("Sunday",    7)
    
    def name(self): return self.value[0]
    def num(self): return self.value[1]
    
    @classmethod
    def sorted_week(cls): return [Day.MON, Day.TUE, Day.WED, Day.THU, Day.FRI, Day.SAT, Day.SUN]

    @classmethod
    def next_day(cls, start_day):
        if start_day == Day.SUN: return Day.MON
        else:
            return Day.sorted_week()[start_day.num()]
                
    @classmethod
    def prev_day(cls, start_day):
        return Day.sorted_week()[start_day.num() - 2]

    @classmethod
    def rand_day(cls): return choice(cls.sorted_week())
            
class Month(Enum):
    JAN = ("January",   1, 31)
    FEB = ("February",  2, 28)
    MAR = ("March",     3, 31)
    APR = ("April",     4, 30)
    MAY = ("May",       5, 31)
    JUN = ("June",      6, 30)
    JUL = ("July",      7, 31)
    AUG = ("August",    8, 31)
    SEP = ("September", 9, 30)
    OCT = ("October",  10, 31)
    NOV = ("November", 11, 30)
    DEC = ("December", 12, 31)
    
    def name(self): return self.value[0]   
    def num(self): return self.value[1]           
    def num_days(self): return self.value[2]

    @classmethod
    def sorted_year(cls): return [Month.JAN, Month.FEB, Month.MAR, Month.APR, Month.MAY, Month.JUN, Month.JUL, Month.AUG, Month.SEP, Month.OCT, Month.NOV, Month.DEC]
    
    @classmethod
    def next_month(cls, start_month):
        if start_month == Month.DEC: return Month.JAN
        else:
            return Month.sorted_year()[start_month.num()]
    
    @classmethod        
    def prev_month(cls, start_month):
        return Month.sorted_year()[start_month.num() - 2]

    @classmethod
    def rand_month(cls): return choice(cls.sorted_year())

class Date:
    
    def __init__(self, day, month, numday, year):
        self.day = day 
        self.month = month
        self.numday = int(numday)
        self.year = int(year)
        
    def next_date(self):
        new_numday = self.numday; new_month = self.month; new_year = self.year
        if self.numday == self.month.num_days(): 
            new_numday = 1
            if self.month == Month.DEC:
                new_year = self.year + 1
            new_month = Month.next_month(self.month)
        else:
            new_numday = self.numday + 1
            
        return Date(Day.next_day(self.day), new_month, new_numday, new_year)
    
    def prev_date(self):
        new_numday = self.numday; new_month = self.month; new_year = self.year
        if self.numday == 1:
            new_numday = Month.prev_month(self.month).num_days()
            if self.month == Month.JAN:
                new_year = self.year - 1
            new_month = Month.prev_month(self.month)
        else:
            new_numday = self.numday - 1
            
        return Date(Day.prev_day(self.day), new_month, new_numday, new_year)

    @classmethod
    def find_month_start_date(cls, start_date):
        count_date = start_date
        if count_date.numday == 1: return count_date
        else:
            while count_date.numday > 1: count_date = count_date.prev_date()
            return count_date

    #Returns the first day of the month preceding the month of the argument
    @classmethod
    def prev_month(cls, start_date):
        cur_date = start_date
        while cur_date.numday > 7:
            cur_date = cls.Date(cur_date.day, cur_date.month, cur_date.numday - 7, cur_date.year)

        while start_date.month == cur_date.month:
            cur_date = cur_date.prev_date()

        backwards_days = (cur_date.numday % 7) - 1
        if backwards_days == -1: backwards_days = 6

        count_day = cur_date.day
        for count in range(0, backwards_days):
            count_day = Day.prev_day(count_day)

        return Date(count_day, cur_date.month, 1, cur_date.year)

    #Returns the first day of the month following the month of the argument
    @classmethod
    def next_month(cls, start_date):
        cur_date = start_date
        while cur_date.month.num_days() - cur_date.numday > 7: cur_date = Date(cur_date.day, cur_date.month, cur_date.numday + 7, cur_date.year)

        while cur_date.month == start_date.month: cur_date = cur_date.next_date()

        return cur_date

    def correct_day(self, start_date):
        cur_date = start_date
        if self.month.num() == cur_date.month.num():   cur_date = Date.find_month_start_date(cur_date)
        while self.month.num() < cur_date.month.num(): cur_date = Date.prev_month(cur_date)
        while self.month.num() > cur_date.month.num(): cur_date = Date.next_month(cur_date)

        while cur_date.numday < self.numday: cur_date = cur_date.next_date()

        cur_day = cur_date.day
        years_diff = cur_date.year - self.year #Positive: count backwards, Negative: count forwards, Zero: you're already there

        if years_diff > 0:
            years_diff = years_diff % 7
            for n in range(0, years_diff): cur_day = Day.prev_day(cur_day)
            self.day = cur_day
        elif years_diff < 0:
            years_diff = abs(years_diff) % 7
            for n in range(0, years_diff): cur_day = Day.next_day(cur_day)
            self.day = cur_day
        else:
            self.day = cur_day

    @classmethod
    def rand_date_wrong_day(cls, start_year):
        m = Month.rand_month()
        return Date(Day.rand_day(), m, randint(1, m.num_days()), randint(start_year - 10, start_year + 10))

                
    def __eq__(self, date):
        return self.day == date.day and self.month == date.month and self.numday == date.numday and self.year == date.year
        
    def __str__(self): return self.day.name() + ' ' + self.month.name() + ' ' + str(self.numday) + ', ' + str(self.year)

'''  
date = Date(Day.MON, Month.JAN, 1, 2000)
for i in range(0, 1000):
    print(str(date))
    date = date.next_date()
'''

'''
test_year = 2006
test_epoch = Date(Day.MON, Month.APR, 20, test_year)
r_date = Date.rand_date_wrong_day(test_year)
print('Before: ' + str(r_date))
r_date.correct_day(test_epoch)
print('After: ' + str(r_date))
'''