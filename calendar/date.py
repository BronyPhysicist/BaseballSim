'''
Created on Dec 1, 2016

@author: Brendan Hassler
'''
from enum import Enum

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
            
    def __eq__(self, date):
        return self.day == date.day and self.month == date.month and self.numday == date.numday and self.year == date.year
    
    def __str__(self): return self.day.name() + ' ' + self.month.name() + ' ' + str(self.numday) + ', ' + str(self.year)

'''  
date = Date(Day.MON, Month.JAN, 1, 2000)
for i in range(0, 1000):
    print(str(date))
    date = date.next_date()
'''