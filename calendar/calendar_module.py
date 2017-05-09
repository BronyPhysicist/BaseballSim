from date import Day
from date import Month
from date import Date

start_date = Date(Day.WED, Month.APR, 1, 2006)

#Consider moving to calendar_window?
def fill_rows_cols(start_date, builder):
	start_row = int(start_date.numday / 7) + 1
	start_col = start_date.day.num()
	cur_date = start_date
	for row in range(1, 7):
		for col in range(1, 8):
			if (row <= start_row and col < start_col) or start_date.month != cur_date.month:
				builder.get_object('Date' + str(row) + str(col)).set_text('\n\n')
			else:
				builder.get_object('Date' + str(row) + str(col)).set_text(str(cur_date.numday) + '\n\n')
				cur_date = cur_date.next_date()

def render_calendar(start_date, builder):
	builder.get_object('month').set_text(str(start_date.month.name()) + ' ' + str(start_date.year))
	fill_rows_cols(start_date, builder)